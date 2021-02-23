# Imports and Classes

One major programming concept that has emerged in modern programming languages is **Object Orientation**. We shall cover that in this part. First let us also briefly cover the ```Import``` feature in python.

## Imports

One of the biggest advantages of python is that it has a huge collection of modules and libraries for performing all sorts of different tasks. A module is a simple python file, which could be imported (i.e. 'included') in other modules or even imported by the user in their own python file. Libraries or packages are essentially just a bundle of related modules. You can directly import a whole library as well, rather than just a single module at a time. We use the ```import``` keyword to include/import a module or library in a python file.

```py
import math                     # imports the math module
print(math.sin(math.pi / 2))    # using the math module in your code

import mysql.connector as sql   # the 'as' keyword can be used to
                                # have the ability to use the module/library
                                # more conveniently in your code
password = input("Enter password: ")
db = sql.connect(host='localhost', user='root', passwd=password)
```

You can use the ```from``` keyword when you only want to import a specific part of a module, such as one or more functions. This is recommended especially when you only need a particular function from some module, because importing the entire module could be a waste of processing time for your program during execution.

```py
from math import sin                    # to only import the sin function
print(sin(1))

from os import listdir, system, getcwd  # to import more than one function
mypath = getcwd()
system("cls")
print(listdir(mypath))
print("\nCWD Path: " + mypath)
```

## The \__name\__ variable

Python has some special built-in variables. They are written with double underscores on both sides so that the python interpreter can recognise them to be special built-in variables rather than ordinary user defined variables. The most well known of these is the ```__name__``` variable. It contains the name of the module within which you imported this file. However, if you run the file directly, then the variable ```__name__``` for that file is assigned the value "__main__" instead. This helps you distinguish between a file that is executed directly, from a file that was *imported into a file which was executed directly*, and hence got indirectly executed as well.

For example, let's say we write two python files, one called "myfile.py" and the other called "smallfile.py". We shall import "smallfile.py" into "myfile.py".

```py
# Source code of "myfile.py"
# -----------------------------------------------------------------------

import smallfile    # assuming that both "smallfile.py" and
                    # "myfile.py" are in the same directory

def f1():
    # some code

def f2():
    # some code

'''
---------
---------
SOME CODE WRITTEN OUTSIDE
OF ALL FUNCTIONS.
THIS CODE WILL JUST GET EXECUTED DIRECTLY WHEN
THIS FILE IS RUN.
---------
---------
'''
```
```py
# Source code of "smallfile.py"
# -----------------------------------------------------------------------

# No code written outside functions
# because this file is meant to only be imported
# You don't want anything to run in case someone runs this file

def F1():
    # some code

def F2():
    # some code

def main():     # the purpose of this function is somewhat synonymous
                # to the main() function in C/C++
    
    '''
    Here, you can write the code that you
    would've otherwise written outside of all
    functions.
    You can use the F1 and/or F2 function(s) from here.
    '''

# Run the program only if it has been imported
# in some module and that module was run.
# (In this example, the module will be "myfile.py")

if __name__ == '__main__':
    pass
else:
    main()
```

## Classes