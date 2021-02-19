// Translation of Minesweeper.cpp from C++ to C
// Translated on 20/02/2021 by Rachit Dhar

#include <stdio.h>
#include <stdlib.h> // for: system(), rand(), srand()
#include <time.h> // for time()

#define ROWS 9
#define COLUMNS 9
#define PROBABILITY 0.15 // probability of a square having a mine

/*

gamestate is a 2D array.
Meanings of different values:

0 to 8 : Number to be displayed on the square, expressing the no. of mines around that square
-1 : Unclicked square
-2 : Unclicked AND has mine

*/

// 2D array storing the game's current state
int gamestate[ROWS][COLUMNS];

// creating a boolean datatype
enum bool { false, true };


// struct to create arrays to store neighbours of a square
struct Square
{
    int nbrs[9][2];
};


// to put mines in the grid after first square has been clicked
void put_mines(int* firstmove)
{
    for (int i = 0; i < ROWS; i++)
    {
        for (int j = 0; j < COLUMNS; j++)
        {
            if (!(i == *firstmove && j == *(firstmove + 1)))
            {
                double randnum = (double)rand() / RAND_MAX;
                                
                if (randnum < PROBABILITY)
                    gamestate[i][j] = -2;
            }
        }
    }   
}


// program to ask user to enter the move (i.e. square to be pressed)
int* askmove()
{
    static int move[2];

    printf("\n");
    printf("Input coordinates of the square you want to click\n");

    for (int i = 0; i < 2; i++)
    {
        int N;
        char *DIRECTION;

        if (i == 0)
            { N = ROWS; DIRECTION = "ROW"; }
        else
            { N = COLUMNS; DIRECTION = "COLUMN"; }

        while (1)
        {
            printf("Enter the %s NUMBER: ", DIRECTION);
            int error_check = scanf("%d", &move[i]);
            
            if (error_check == EOF) // in case value entered in not an integer
            {
                printf("Invalid input! Try again\n\n");
            }
            else
            {
                if (move[i] < 1 || move[0] > N)
                    printf("Invalid %s number! Try again\n\n", DIRECTION);
                else
                    break;
            }
        }
    }    

    // convert the array to assume rows and columns are starting from 0
    move[0] -= 1;
    move[1] -= 1;

    return &move[0];
}


// return a struct to get all neighbours of a given square
struct Square get_neighbours(int* move)
{
    int i = *move;
    int j = *(move + 1);
    
    struct Square nbs;   
    int n = 1; // n tells the number of total neighbours that the square has

    for (int x = 0; x < 2; x++)
    {
        int N, M;

        if (x == 0)
            { N = 0; M = -1; }
        else
            { N = ROWS - 1; M = 1; }
        
        if (i != N)
        {
            nbs.nbrs[n][0] = i + M;
            nbs.nbrs[n][1] = j;
            n += 1;
            
            if (j != 0)
            {
                nbs.nbrs[n][0] = i + M;
                nbs.nbrs[n][1] = j - 1;
                n += 1;
            }
            
            if (j != (COLUMNS - 1))
            {
                nbs.nbrs[n][0] = i + M;
                nbs.nbrs[n][1] = j + 1;
                n += 1;
            }
            
        }
    }

    if (j != 0)
    {
        nbs.nbrs[n][0] = i;
        nbs.nbrs[n][1] = j - 1;
        n += 1;
    }
    
    if (j != (COLUMNS - 1))
    {
        nbs.nbrs[n][0] = i;
        nbs.nbrs[n][1] = j + 1;
        n += 1;
    }
    
    
    nbs.nbrs[0][0] = n - 1; // store the number of neighbours at index 0,0
    nbs.nbrs[0][1] = 0; // just an arbitrary useless index

    return nbs;
}


// click an unclicked square,
// and if it is a 0 number square, then click all unclicked squares around it as well

void click(int* move)
{
    if (gamestate[*move][*(move + 1)] == -1)
    {
        struct Square nbs = get_neighbours(move);
        
        int total_nbrs = nbs.nbrs[0][0];
        int num_mines = 0;
        
        for (int i = 1; i <= total_nbrs; i++)
            if (gamestate[nbs.nbrs[i][0]][nbs.nbrs[i][1]] == -2)
                num_mines += 1;
        
        gamestate[*move][*(move + 1)] = num_mines;
        
        
        if (num_mines == 0)
        {
            for (int i = 1; i <= total_nbrs; i++) 
                click(&nbs.nbrs[i][0]);
        }
    }
}


// update the grid and return whether win, loss, or already clicked
int update_gamestate(int* move)
{
    if (gamestate[*move][*(move + 1)] == -2) // clicked a mine
        return -1;
    else if (gamestate[*move][*(move + 1)] != -1) // clicked an already clicked square
        return -2;
    else
    {
        click(move);
        
        enum bool won = true;
        for (int i = 0; i < ROWS; i++)
            for (int j = 0; j < COLUMNS; j++)
                if (gamestate[i][j] == -1) { won = false; }

        if (won == true)
            return 1;
        else
            return 0;
    }
}


// GRID APPEARANCE DESIGN
/*
    Supposed to look this way:

     	  1   2   3   4   5   6   7

        -----------------------------
    1	| 1 | 2 | 0 |   |   | 0 | 3 |
        -----------------------------
    2	|   |   | 0 | 0 |   |   | 2 |
        -----------------------------
*/

// printing the horizontal line
void horiz_line()
{
    for (int i = 0; i < (4 * COLUMNS + 1); i++)
        printf("-");
    
    printf("\n");
}

// program to display the grid from the current gamestate
void printgrid(int result)
{ 
    printf("\t  1");
    for (int i = 1; i < COLUMNS; i++)
        printf("   %d", i + 1);

    printf("\n\n \t");
    horiz_line();

    // printing rows of the grid

    for (int i = 0; i < ROWS; i++)
    {
        printf("%d\t|", i + 1);

        for (int j = 0; j < COLUMNS; j++)
        {
            if (gamestate[i][j] == -1) // unclicked square
                printf("   |");
            else if (gamestate[i][j] == -2) // square with mine
            {
                if (result == -1)
                    printf(" X |"); // display mines as 'X' when you lose
                else if (result == 1)
                    printf(" # |"); // display mines as '#' when you win
                else
                    printf("   |"); // otherwise treat as unclicked squares
            }
            else
                printf(" %d |", gamestate[i][j]); // clicked squares (with numbers 0 to 8)
        }

        printf("\n \t");
        horiz_line();
    }

}


// program to begin the new game
void startgame()
{
    // print updated grid (or break, in case of win or loss)
    // and then ask for entering next move

    enum bool start = true;
    enum bool finished = false;

    while (1)
    {
        printgrid(0);
        
        // for the first move, there should not be any mines.
        // Mines are assigned after first move
        
        if (start == true)
        {
            int *firstmove = askmove();
            put_mines(firstmove);
            int result = update_gamestate(firstmove);
            
            start = false;
        }
        else
        {
            while (1)
            {
                int *move = askmove();
                int result = update_gamestate(move);

                if (result == 1) // win
                {
                    system("cls");
                    printgrid(1);

                    printf("\nYOU WIN !!!\n");
                    finished = true;
                    break;
                }
                else if (result == -1) // lost
                {
                    system("cls");
                    printgrid(-1);

                    printf("\nTHAT WAS A MINE! YOU LOSE !!!\n");
                    finished = true;
                    break;
                }
                else if (result == -2) // clicked an already clicked square
                {
                    printf("This square is already clicked! Try again\n\n");
                }
                else
                    break;
            }
            
            if (finished == true)
                break;
        }

        system("cls");
        
    }
}


// program starts execution here
int main()
{
    enum bool check = false;
    srand((unsigned) time(0));
 
    do
    {
        // initialize gamestate
        for (int i = 0; i < ROWS; i++)
            for (int j = 0; j < COLUMNS; j++)
                gamestate[i][j] = -1;
        
        // start a new game
        system("cls");
        startgame();

        // when game gets over, ask for new game
        char response;

        while (1)
        {
            printf("Do you want to play a new game? (y/n): ");

            // flush any input still in the stdin buffer, before calling scanf
            char c = '\0';
            while (c != '\n' && c != EOF)
                c = getchar();

            scanf("%c", &response);

            if (response == 'y' || response == 'Y')
                { check = true; break; }
            else if (response == 'n' || response == 'N')
                { check = false; break; }
            else
                printf("Sorry, wrong input. You must enter either \'y\' or \'n\'\n");
        }

    } while (check == true);
    
    return 0;
}
