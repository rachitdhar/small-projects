# Project started on 13/11/2020
# Completed on 14/11/2020
# Creator: Rachit Dhar

import mysql.connector as sql
import getpass
import random
import math
import time

db = object()

# get password and connect to mysql
while True:
    try:
        pword = getpass.getpass()
        db = sql.connect(host="localhost", user="root", password=pword)
        break
    except:
        print("Wrong password. Try again.")

cursor = db.cursor()

# If database does not exist, then create one
try:
    cursor.execute('use tictactoe')
    db.commit()
except:
    cursor.execute('create database tictactoe')
    db.commit()
    cursor.execute('use tictactoe')
    db.commit()

# display info
print("\n--------------- Tic Tac Toe Game -----------------\n")
print("This game shall be played on a 3x3 grid.")
print("Different positions on the grid have been assigned, ")
print("unique numbers which you shall use to play a move at")
print("that position. These numbers are as follows:\n")

# function to create and display a grid from a given gamestate
def displaygrid(gamestate):
    for i in range(3):
        print("-------------")
        print("| "+gamestate[i][0]+" | "+gamestate[i][1]+" | "+gamestate[i][2]+" |")
    print("-------------\n")

displaygrid([['1','2','3'],['4','5','6'],['7','8','9']])
print("In this game, X plays first.")

# to tell who's move it currently is (based on current gamestate)
def whosmove(gamestate):
    numX = 0
    numO = 0
    for i in range(3):
        for j in range(3):
            if gamestate[i][j] == "x":
                numX += 1
            elif gamestate[i][j] == "o":
                numO += 1
    
    if numX == numO:
        return "x"
    else:
        return "o"

# to check if given gamestate is won or not
def checkwin(gamestate):
    g = gamestate
    won = False

    # check horizontally and vertically
    for i in range(3):
        if ((g[i][0] == g[i][1] == g[i][2] != " ")) or ((g[0][i] == g[1][i] == g[2][i] != " ")):
            won = True
            break

    # check diagonals
    if (g[0][0] == g[1][1] == g[2][2] != " ") or (g[2][0] == g[1][1] == g[0][2] != " "):
        won = True

    return won

# to check whether game is a tie
def checkdraw(gamestate):
    draw = True

    for i in range(3):
        for j in range(3):
            if gamestate[i][j] == " ":
                draw = False
    
    return draw

# to find sql table associated with current gamestate
def table(gamestate):
    tablename = "table_"

    for i in range(3):
        for j in range(3):
            if gamestate[i][j] != " ":
                pos = 1 + (i*3) + j
                tablename += (str(pos) + gamestate[i][j])

    return tablename

# function to create an sql table for a given gamestate
def maketable(gamestate, tablename):
    cursor.execute('create table '+tablename+'(Available_Moves integer, Win_Potential integer)')
    db.commit()

    for i in range(3):
        for j in range(3):
            if gamestate[i][j] == " ":
                pos = 1 + (i*3) + j
                cursor.execute('insert into '+tablename+' values('+str(pos)+',0)')
                db.commit()

# list of tables to keep track of moves played by AI
AIhistory = list()

# given a certain gamestate, the AI shall calculate the best move, play it, and return new gamestate
def AIplays(gamestate):
    tablename = table(gamestate)
    moves = list()

    try:
        cursor.execute('select* from '+tablename)
        moves = cursor.fetchall()
    except:
        maketable(gamestate, tablename)
        cursor.execute('select* from '+tablename)
        moves = cursor.fetchall()

    zeroexists = False
    for move in moves:
        if int(move[1]) == 0:
            zeroexists = True

    calculated_move = int()
    if zeroexists == True:
        chooserow = random.randint(1, len(moves))
        calculated_move = int(moves[chooserow - 1][0])

        AIhistory.append([tablename, calculated_move])
    else:
        win_potential = -math.inf
        for move in moves:
            if int(move[1]) > win_potential:
                calculated_move = int(move[0])
                win_potential = int(move[1])

        AIhistory.append([tablename, calculated_move])

    i = int((calculated_move/3) - 0.1)
    j = calculated_move - (i*3) - 1

    symbol = whosmove(gamestate)
    gamestate[i][j] = symbol

    return gamestate

# to check if certain moves are 'clearly' winning(return 1)/losing(return -1), else return 0
def move_eval(tablename, move):
    cursor.execute('select* from '+tablename+' where Available_Moves = '+str(move))
    evaluation = cursor.fetchall()[0][1]

    if evaluation > 1000:
        return 1
    elif evaluation < -100:
        return -1
    else:
        return 0

# show training progress
def progressbar(current, total):
    progress = float(current) / total
    fulllen = 50
    currentlen = int(progress * fulllen)

    endchar = str()
    if current == total - 1:
        endchar = '\n'
    else:
        endchar = '\r'
    
    print("Progress: |"+"▯"*currentlen+" "*(fulllen - currentlen)+"| "+("{0:.5f}").format(progress*100)+" % complete", end=endchar)

# function to train the AI (using AI vs AI games)
def trainAI(games):
    for i in range(games):
        progressbar(i, games)
        gamestate = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        AIhistory.clear()

        while True:
            gamestate = AIplays(gamestate)
            if checkwin(gamestate) == True:
                loser = whosmove(gamestate)

                if loser == "x":
                    i = 0
                    for table in AIhistory:
                        tablename = table[0]
                        move = table[1]

                        if i % 2 == 0:
                            decrement = i + 1
                            if move_eval(tablename, move) != -1:
                                cursor.execute('update '+tablename+' set Win_Potential = (Win_Potential - '+str(decrement)+') where Available_Moves = '+str(move))
                                db.commit()
                        else:
                            increment = i*3
                            if move_eval(tablename, move) != 1:
                                cursor.execute('update '+tablename+' set Win_Potential = (Win_Potential + '+str(increment)+') where Available_Moves = '+str(move))
                                db.commit()
                        i += 1
                else:
                    i = 0
                    for table in AIhistory:
                        tablename = table[0]
                        move = table[1]

                        if i % 2 == 0:
                            increment = i*3 + 1
                            if move_eval(tablename, move) != 1:
                                cursor.execute('update '+tablename+' set Win_Potential = (Win_Potential + '+str(increment)+') where Available_Moves = '+str(move))
                                db.commit()
                        else:
                            decrement = i
                            if move_eval(tablename, move) != -1:
                                cursor.execute('update '+tablename+' set Win_Potential = (Win_Potential - '+str(decrement)+') where Available_Moves = '+str(move))
                                db.commit()
                        i += 1
                break
            elif checkdraw(gamestate) == True:
                break
    
        try:
            cursor.execute('update AI_Learning set Games_Practiced = Games_Practiced + 1')
            db.commit()
        except:
            cursor.execute('create table AI_Learning(Games_Practiced bigint)')
            db.commit()
            cursor.execute('insert into AI_Learning values(1)')
            db.commit()

# function for user vs AI game
def playgame(choice):
    gamestate = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    AIhistory.clear()
    print("\n------------- Game Begins --------------\n")
    
    if choice == 'x':
        displaygrid(gamestate)
        while True:
            try:
                move = int(input("Enter your move: "))
                if 1 <= move <= 9:
                    i = int((move/3) - 0.1)
                    j = move - (i*3) - 1
                    if gamestate[i][j] == " ":
                        gamestate[i][j] = choice
                        print("")
                        displaygrid(gamestate)
                        break
                    else:
                        print("This position is already filled. Try again")
                else:
                    print("Your move must be an integer from 1 to 9. Try again")
            except:
                print("Your move must be an integer from 1 to 9. Try again")

    while True:
        gamestate = AIplays(gamestate)
        print("My Move:\n")
        displaygrid(gamestate)

        if checkwin(gamestate) == True:
            print("I Win!")
            print("----------------------------------------\n")
            
            i = 0
            for table in AIhistory:
                tablename = table[0]
                move = table[1]

                increment = i*3 + 1
                if move_eval(tablename, move) != 1:
                    cursor.execute('update '+tablename+' set Win_Potential = (Win_Potential + '+str(increment)+') where Available_Moves = '+str(move))
                    db.commit()
                i += 2

            break
        elif checkdraw(gamestate) == True:
            print("Game Tied!")
            print("----------------------------------------\n")
            break
        else:
            while True:
                try:
                    move = int(input("Enter your move: "))
                    if 1 <= move <= 9:
                        i = int((move/3) - 0.1)
                        j = move - (i*3) - 1
                        if gamestate[i][j] == " ":
                            gamestate[i][j] = choice
                            print("")
                            displaygrid(gamestate)
                            break
                        else:
                            print("This position is already filled. Try again")
                    else:
                        print("Your move must be an integer from 1 to 9. Try again")
                except:
                    print("Your move must be an integer from 1 to 9. Try again")

            if checkwin(gamestate) == True:
                print("You Win!")
                print("----------------------------------------\n")
                
                i = 0
                for table in AIhistory:
                    tablename = table[0]
                    move = table[1]

                    decrement = i + 1
                    if move_eval(tablename, move) != -1:
                        cursor.execute('update '+tablename+' set Win_Potential = (Win_Potential - '+str(decrement)+') where Available_Moves = '+str(move))
                        db.commit()
                    i += 2

                break
            elif checkdraw(gamestate) == True:
                print("Game Tied!")
                print("----------------------------------------\n")
                break
    
    try:
        cursor.execute('update AI_vs_Human set Games_Played = Games_Played + 1')
        db.commit()
    except:
        cursor.execute('create table AI_vs_Human(Games_Played integer)')
        db.commit()
        cursor.execute('insert into AI_vs_Human values(1)')
        db.commit()

# ask user for choice of side
while True:
    while True:
        print("Choose your side")
        choice = input("X or O ?: ")
        
        if choice.lower() == 'x':
            playgame("x")
            break
        elif (choice.lower() == 'o') or (choice.lower() == '0'):
            playgame("o")
            break
        elif choice.lower() == "t":
            while True:
                try:
                    games = int(input("Enter number of training iterations (no. of games): "))
                    print("Training...")
                    starttime = time.time()
                    trainAI(games)
                    endtime = time.time()
                    print("Time taken: "+str(endtime - starttime)+" seconds")
                    break
                except:
                    print("Invalid input. Enter an integer")
            print("AI trained successfully\n")

            cursor.execute('select* from AI_Learning')
            games_trained = cursor.fetchall()[0][0]
            print("Trained by playing against itself and learning")
            print("("+ str(games_trained) + " games played against itself till now)\n")
        elif choice.lower() == "del_memory":
            # to delete the AIs memory (i.e. all that it has ever learnt) and start from scratch
            print("Deleting memory...")
            cursor.execute('drop database tictactoe')
            print("Memory cleared successfully.")
            cursor.execute('create database tictactoe')
            db.commit()
            cursor.execute('use tictactoe')
            db.commit()
        else:
            print("Sorry, invalid choice. Try again\n")
    print('\n')

    conti = True
    while True:
        conti = input("Do you want to play a New Game? (Y/N): ")
        if conti.lower() == 'n':
            conti = False
            break
        elif conti.lower() == 'y':
            break
        else:
            print("Invalid input. Try again")

    if conti == False:
        break
    else:
        print('\n')
