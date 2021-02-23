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

## Classes