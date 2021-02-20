# Functions and File Handling

In the previous part, we have covered the logic statements that are used for python programming. Now we can learn about two more concepts that are fundamental to any programming language: Functions and File Handling.

## Functions

At the simplest level, a function is simply a block of code that you define, and then use wherever you need to use it. We use the ```def``` keyword to create a function

```py
def myfunction(): # the name of this function is "myfunction"
    '''
    Some code written
    inside this
    function
    '''
```

The program *does not* run the code inside the function on its own. A function's purpose is to only define what code it is supposed to execute *when that function gets called*. 'Calling' a function basically means 'running that function'. We call a function by using the name of that function.

```py
def print_hello():
    print("Hello, world!")

print_hello()   # calling the function
                # (this will cause "Hello, world!" to be printed)
```

A function can also be defined with one or more parameters. When you want to use (i.e. 'call') this function, you must provide value(s) inside the parenthesis for the function to work with. These input values are called arguments.

```py
def print_line(sentence):       # sentence is the parameter
    print(sentence)

print_line("Hello, world!")     # "Hello, world!" is the argument
```

An example using multiple parameters:

```py
def add(num1, num2):    # num1 and num2 are 'parameters'
    print(num1 + num2)

add(3, 7)               # Here, 3 and 7 are 'arguments'
                        # The output is: 10
```

One of the most important features of a function is the ability to not only execute a block of code, but to also return some output to the program itself, when it is executed. A function can return values to the program using the ```return``` keyword.

```py
def multiply(num1, num2):
    return (num1 * num2)

product = multiply(3, 8)    # the function calculates 3 * 8, and returns 24
                            # which is then stored in the variable 'product'
```

Another example of using 'return':

```py
def vote_eligibility(age):

    if age >= 18:
        return "You can vote!"
    else:
        return "Sorry, you cannot vote!"

user_age = int(input("Enter your age: "))
print(vote_eligibility(user_age))       # the function returns the appropriate string
                                        # and that string is then printed by the print() function
```

In programming, there is a very popular concept related to functions, called *Recursion*. As the name may suggest, it involves using the function within itself! Often this is a very powerful technique indeed:

```py
# A function to calculate the factorial of a number

def factorial(n):

    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))
```

There is another capability that python provides, which is not so commonly used, but may be suitable in rare circumstances. It is the usage of **Nested Functions**. These are usually only used when you want to divide a complex task into several subtasks where those individual subtasks have no meaning outside the main function. Lexically, nested functions are a form of Information hiding.

```py
# function that sorts a list of numbers that the user enters
def sort_nums():

    # embedded function within original function
    def get_nums():

        nums = list()

        while True:
            while True:
                try:
                    num = int(input("Enter number: "))
                    nums += [num]
                    break
                except:
                    print("Invalid input! Try again")
            
            check = True

            while True:
                more_nums = input("Do you want to enter another number? (y/n): ")
                
                if more_nums.lower() == "y":
                    check = True
                    break
                elif more_nums.lower() == "n":
                    check = False
                    break
                else:
                    print("Invalid input! Try again")
            
            if check == False:
                break
        
        return nums


    # now working within the original function again
    nums = get_nums()
    n = len(nums)

    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print(nums)
```

## Local and Global Scope

When you create a variable outside of any function, then that variable is going to persist throughout the rest of the program, and most importantly, *it can be accessed anywhere in the entire program*. Such a variable is called a **Global scope variable**.

However, if you create a variable *within a function*, then that variable only exists during the execution of that function's code (which happens when that function gets called). Most importantly, *you cannot access this variable from anywhere outside that function*. It can only be accessed from within that function. Such a variable is called a **Local scope variable**.

```py
list_of_names = list() # list_of_names is Global scope

def add_names():

    num = int(input("How many names do you want to enter: ")) # num is Local scope

    for i in range(num):
        name = input("Enter name: ")
        list_of_names += [name]

add_names()
```

Even in general, if your variable has been defined inside *any indented block*, it cannot be accessed from outside that indented block.

```py
for i in range(3):
    name = input("Enter name: ")    # name is Local scope. 
                                    # It cannot be accessed outside this 'for loop'
    print(f"Hello {name}!\n")
```

## File Handling

