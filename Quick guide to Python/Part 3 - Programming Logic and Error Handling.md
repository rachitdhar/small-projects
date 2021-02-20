# Programming Logic and Error Handling

Now that we have covered the basics in parts 1 and 2, we will study the actual implementation of logic in python programming, using which we can create algorithms to solve problems. After that, we will briefly cover Error handling in python as well. The topics to be covered are:

1. Decision making (Control flow)
2. For Loop
3. While Loop
4. Jump Statements
4. Error Handling

## Decision making (Control Flow)

In python, decision making is done through ```if, elif, else``` keywords. (elif is supposed to stand for "else if"). We use these for *conditional programming*. We can provide conditions such that a statement or group of statements will be executed only when those conditions hold true

```py
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

We use 'else' keyword when we want to execute something when *no other condition holds true*. Sometimes, we may not want to execute anything when the condition is false. In such cases, we don't need to use the 'else' keyword.

The 'elif' keyword is used when we have 2 or more conditions. We can use multiple 'elif's for multiple conditions.

```py
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif 90 > marks >= 80:
    print("Grade B")
elif 80 > marks >= 50:
    print("Grade C")
elif 50 > marks >= 30:
    print("Grade D")
else:
    print("Fail")
```

## For Loop

Sometimes we want to execute the same statement (or set of statements) multiple times. A logical statement that gives the instruction to execute some block of code multiple times is called a "Loop Statement", and this process is called Looping.

Usually, when we know how many times we want to execute the same statement, we use the 'for loop'.

```py
for i in [1,2,3]:
    print("Hello world!")

'''
Output:
----------------
Hello world!
Hello world!
Hello world!
'''
```

The working of the 'for' statement is as follows: When we write ```for i in [1,2,3]```, the program first assigns ```i = 1``` and executes the block of code, then it takes ```i = 2``` and executes the same block of code, and finally it takes ```i = 3``` and executes the block again.

In the above program, since we did not use ```i``` inside the block of code, so it is called a "Dummy variable". Thus, in this case we could have had any 3 elements inside our list, and the program would still give the same result:

```py
for i in ["apple", "ball", "cat"]:
    print("Hello world!")

'''
Output:
----------------
Hello world!
Hello world!
Hello world!
'''
```

We can also write a program where we make use of the 'for loop' variable.

```py
for i in [0,1,2]:
    print(i)

'''
Output:
----------------
0
1
2
'''
```

Actually, python provides a special function to make the generation of lists easier. This comes handy, because as you can imagine, it is very impractical to manually write out a list of 100 or even 1000 elements in case it's required! (Moreover, you might want to ask the user for the number of times you want to run the loop, and in that case the length of the list would be stored in a variable, so it's impossible to even make the list!)

This is the ```range()``` function. range() can return lists of a sequence of numbers as specified in the argument inside the parenthesis of the function:

```py
range(3)            # Same as [0,1,2]
range(1)            # Same as [0]
range(100)          # Same as [0,1,2,3,4,...,99]

range(2, 6)         # Same as [2,3,4,5]
range(0, 100)       # Same as [0,1,2,3,4,...,99]
range(5, 20, 2)     # Same as [5,7,9,11,13,15,17,19]. Here the third number tells the INCREMENT VALUE
range(50, 0, -10)   # Same as [50,40,30,20,10]
```

Using this function, we can create 'for' loops easily:

```py
num = int(input("Enter the number of names you want to enter: "))
list_of_names = list()

for i in range(num):
    name = input("Enter a name: ")
    list_of_names += [name]

# display the list of all names entered by user
print(list_of_names)
```

You can also use loops within loops. This is called "Nested Looping". When a for loop is nested within another for loop, it is called a 'Nested For Loop'.

```py
for i in range(3):
    print(f"Table of {i+1}")
    print("----------------------")

    for j in range(10):
        print(f"{i+1} x {j+1} = {(i+1)*(j+1)}")

    print() # to create a gap between two tables
```
```
Output
=============================
Table of 1
----------------------
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

Table of 2
----------------------
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

Table of 3
----------------------
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

## While Loop

In order to execute a block of code *while a certain condition holds true*, we use the 'while' loop.
Sometimes, a while loop could be converted to a for loop that performs the same action, and vice-versa.

```py
i = 1

while i < 10:
    print(i)
    i += 1
```
```
Output
=====================
1
2
3
4
5
6
7
8
9
```

The while loop works as follows: First it checks the condition. If it is true, then the block of code under it gets executed, and we go back to the condition to check it. If it's still true, then the block is executed again, and so on. If the condition returns false, then the block is not executed, and the while loop gets terminated.

Since the condition provided to while loop eventually boils down to either 'true' or 'false', so if desired, we can also *directly pass* ```True``` or ```False``` to it. (Note: We never directly pass a 'false' to the while loop, because the while loop would just immediately get terminated, and so the block of code would *never* get executed. So it basically just makes the entire code pointless!)

```py
while True:
    print("Hello world!")
```

The above code is technically correct, but it should *not* be executed! Because it is an *Infinite Loop*, which will cause the print() statement to execute "Hello world!" forever!!

In Python, there is also a unique feature of using the 'else' keyword after a 'For' or 'While' loop. The code inside 'else' gets executed when the for loop gets over, or when the condition of the while loop returns false, respectively.

```py
i = 1

while i < 9:
    print(i)
else:
    print("Oops! i is not less than 9 anymore!")
```

## Jump Statements

Jump statements are some unique keywords in python that can be used to bypass a certain block of code in a certain specific manner, depending upon which keyword you used. There are three jump keywords in python: ```pass```, ```break``` and ```continue```.

The ```pass``` keyword is actually very simple. It is basically a null statement, i.e. it literally does nothing. The difference between a comment and a pass statement is that the python interpreter completely ignores a comment. But the pass statement is *not* ignored. The statement just doesn't *do* anything. It can be used in places where you must write *something* (i.e. places that you can't leave blank, or else it would produce an error), but you don't want to execute anything.

```py
# to print numbers from 1 to 9, but not 8
i = 1

while i < 10:
    if i == 8:
        pass
    else:
        print(i)

    i += 1

# Note: This is NOT the most efficient way to write this program.
# Alternative solutions exist. This is just an example for demonstration.
```

The next keyword (which is perhaps the most important of them all) is the ```break``` statement. When a break statement is executed inside a loop, it immediately causes the termination of that loop (i.e. any code after the break statement won't be executed if the break statement gets executed, and the program will come out of the loop)

```py
list_of_names = list()

while True:
    name = input("Enter a name: ")
    list_of_names += [name]

    more_names = input("Do you want to enter more names? (y/n): ")

    if more_names.lower() == "n":
        break

# display all the names stored in the list
print(list_of_names)
```

The ```continue``` statement is used inside a loop, when you want to bypass the part of the block of code within the loop that comes after the 'continue' statement, but then go back to the loop condition, and the loop goes on again (i.e. obviously only if the loop condition returns true).

```py
# to print numbers from 1 to 9, but not 8
i = 1

while i < 10:

    if i == 8:
        i += 1
        continue
    
    print(i)
    i += 1

# Note: This is NOT the most efficient way to write this program.
# Alternative solutions exist. This is just an example for demonstration.
```

## Error Handling

Sometimes for some reason you cannot prevent an error from occuring in a program. This may be due to various reasons (for example: the user entering a string, when she/he was supposed to enter an integer). For such scenarios, it becomes very convenient to have a feature that can handle *any* error that occurs within a certain block of code where you expect the possibility of an error to occur.

In python, error handling is performed using a 'Try-Except' block. Here, you enter the error-prone code inside the 'try' block. In case the block of code produces an error during run-time, the program immediately goes to the block of code under the 'catch' statement. The code under 'catch' is supposed to be executed only when an error occurs inside the 'try' block.

You can also *cause an error to occur* on demand, by using the ```raise``` keyword. On doing this, the program will go and execute the code under 'catch' statement, just as if any ordinary error has occured.

```py
age = int()

while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            raise

        break
    except:
        print("Sorry, you must enter a positive integer value")

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```