## Basic I/O

Here we shall read about basic I/O functionalities in python. (I/O stands for Input/Output)\
Firstly, we will see how to print something in python. For this we have the print() function.

```python
print("Hello world!")
```

To make the print() function ignore some character, we can use "\\". Also, we use '\n' for newline and '\t' for getting a tab.

```python
print("To print quotes, we must ignore them this way: \"Hello world!\"")
print("To print a new line do this:\nNow this part should be in the next line")
```

After printing something, the cursor automatically goes to the next line of the console. This happens because python's print() function adds a '\n' to the end of the printed sentence by default. But we can overwrite this to prevent the cursor from going to the next line

```python
print("Hello world!", end='')
```

If we want, we can also make the cursor go to the beginning of the line that we just printed. This is done using the *carriage-return* character '\r'.

```python
print("Hello world!", end='\r')
```

Now, to print variables, we do the following (apply type-casting when required):

```py
age = 15
num_fingers = "ten"

print("I am " + str(age) + " years old")
print("I have " + num_fingers)
```

Python also provides a feature called *f-strings*, to embed the variable within the whole string itself, that sometimes makes this process look more neat (Note: Here we don't need to perform type-casting):

```py
age = 20

print(f"I am {age} years old")
```

Now, for taking input from a user, python provides the input() function:

```py
name = input("Enter your name: ")
```

By default, the input() function returns string datatype. If you want it to return some other datatype, then you must remember to perform type-casting while taking the input:

```py
age = int(input("Please enter your age: "))
```

## Strings

String is a text datatype in python. You can make a string variable in the following ways:

```py
string1 = "hello everyone!"     # The standard preferred way
string2 = 'world'               # An alternative (in some languages, like C, this way is used
                                # to store character datatype intead of strings)
string3 = '''this is python'''  # A docstring
```

The Docstring is generally only used when you want to create multi-line comments in python:

```py
'''
This is a
very very long, and in fact, an
unnecessarily lengthy
sentence, displayed
using a docstring.

Since this is a comment,
it will be ignored completely during execution of the code
'''
```

In most cases, you would probably be satisfied by using simple single line comments!

```py
# Hey there! This is a comment
But this is not a comment, and will lead to an error if you execute this line!
```

In python you have special features called *Indexing and Slicing*. Every character of a string has an index, starting from 0. Negative indexes are used to read the string backwards.

For example: Take the string "Hello world!"

| H | e | l | l | o |   | w | o | r | l | d | ! |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
|-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

You can obtain either single characters, or groups of characters from a string by performing indexing or slicing operations respectively:

```py
name = "Rachit"

print(name[0])          # Indexing. Output will be: R
print(name[4])          # Indexing. Output will be: i
print(name[-1])         # Again indexing. Output will be: t

print(name[0:3])        # Slicing. Output will be: Rac
print(name[0:1])        # Slicing. Output will be: R
print(name[0:5])        # Slicing. Output will be: Rachi
print(name[2:4])        # Slicing. Output will be: ch
print(name[3:5])        # Slicing. Output will be: hi
print(name[-4:-1])      # Slicing. Output will be: chi
print(name[0:])         # Slicing. Output will be: Rachit
print(name[:])          # Slicing. Output will be: Rachit
```

From the above examples of slicing, you must have noticed that when performing slicing, the first index is *included* but the second (closing) index is *excluded*. For example, ```[2:5]``` would mean indexes 2, 3 and 4.

Apart from this, there are several functions and methods in python to perform string operations. Some common ones are: ```len()``` (to get the length of a string), ```.strip(), .split(), .join(), .upper(), .lower(), .title()```, and many more.

Strings can be concatenated together normally using the '+' operator.

```py
str1 = "cat"
str2 = "dog"

s = str1 + str2
print(s) # Output is: catdog
```

## Sequences

Python provided several sequence data types. These are similar to arrays in other languages like C. Nonetheless, they are not the same. The main sequence data types are Lists, Tuples and Sets.

Lists are the most commonly used out of all sequence data types. They happen to be very important in python programming and are required pretty much everywhere. You can perform indexing and slicing on lists and tuples just like you do for strings.

```py
# These all are Lists

fruits = ["apples", "bananas", "mangoes"]
nums = [1, 5, 9, -2, 0, 100]
random_list = ["a", 23, -19, "dogs", True, 9.89]

print(fruits[1])    # Output: bananas
print(fruits[1:])   # Output: ["bananas", "mangoes"]
print(nums[0:3])    # Output: [1, 5, 9]

nums[4] = 89        # Changing value of a list using assignment operator (cannot be done for tuples)
print(nums)         # Output: [1, 5, 9, -2, 89, 100]

fruits += ["guavas"]    # Adding a new element (MUST be enclosed in square brackets)
print(fruits)           # Output: ["apples", "bananas", "mangoes", "guavas"]
```
Tuples are similar to lists in several ways. But a major difference is that tuples are *immutable* (i.e. you cannot change an element of a tuple once it has been assigned to that tuple). You can only add new members to tuples.

```py
t1 = (1, 2, 3)

print(t1[0])    # Output: 1
print(t1[0:])   # Output: (1, 2, 3)

t1 += (4,)      # Adding new element (here we MUST PUT A COMMA after the element inside parenthesis)
print(t1)       # Output: (1, 2, 3, 4)
```

Lists and tuples have special built-in functions and methods as well. The ```len()``` function returns the length of a tuple or a list. The ```.append()``` method can be used to add an element to a list in a more readable manner. ```.sort()``` method is used to get the sorted version of a list.

```py
nums = [1, 4, 3, -2, 0]
num2 = [2, 0, 8, 3]

print(num2.sort()) # Output: [0, 2, 3, 8]

nums.append(8)
print(nums) # Output: [1, 4, 3, -2, 0, 8]

nums.append([2, 3]) # Adding a LIST AS AN ELEMENT OF A LIST
print(nums) # Output: [1, 4, 3, -2, 0, 8, [2, 3]]
```

There is another datatype called Dictionary. It is not exactly a sequence datatype, but it is similar to it. It is actually a "mapping" kind of datatype, which stores key-value pairs

```py
dict1 = {1:100, 2:300, 3:124}
d = {12:"abc", 89:"e"}
phonebook = {"Alex":12345, "Bob":67890, "Cathy":24680, "Greg":13579}

print(phonebook["Bob"])     # Output: 67890

print(phonebook.keys())     # Output: ["Alex", "Bob", "Cathy", "Greg"]
print(phonebook.values())   # Output: [12345, 67890, 24680, 13579]
```

In python, there is a concept called *Constructors* for all objects, which can be used to create that object and assign it to a variable instead of giving a value immediately (this is somewhat similar to the "declaration" of a variable, as done in C language)

```py
fruits = list()         # Same as saying: fruits = []
nums = tuple()          # Same as saying: nums = ()
phonebook = dict()      # Same as saying: phonebook = {}

# similarly these are also valid
a = int()
n = float()
text = str()

# Weirdly, if you DON'T EVEN KNOW the DATATYPE, you can STILL create a variable
# This unknown object is gonna be called .... well, object()

unknown_var = object() # later on you could assign this a value of any datatype
```

## Multidimensional Sequences

Sometimes it becomes necessary to use multidimensional sequences (usually lists). These are often 2-dimensional sequences. They can be of many kinds: Lists within lists, Tuples within Tuples, Lists within tuples, Tuples within lists, or some mixture where every element is not of the same datatype.

There are 2 main ways in which we usually write 2-dimensional sequences

```py
# Lists within list

phonebook1 = [["Adam", 12345], ["Eve", 67890]] # First way of writing

# The second way of writing (a more 'clean' way)
phonebook2 = [
    ["Carl", 13579],
    ["Douglas", 24680]
]

# Tuples within List

days_of_week = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday")
]
```

There are several uses of multidimensional sequences. Often they can be used to represent some kind of practical scenario in a virtual manner. For example, we can use them to represent a game of tic tac toe:

```py
# a variable "gamestate"

gamestate = [
    ['X', 'O', 'X'],
    ['X', 'X', 'O'],
    ['O', 'X', 'O']
]

# These values are being shown just as an example.
# In an actual program, these values would be entered into the 2D list by the user
# during run-time itself

gamestate[1][2] = 'X' # Assigning value to a 2D list

'''
Now it would look like this:

gamestate = [
    ['X', 'O', 'X'],
    ['X', 'X', 'X'],
    ['O', 'X', 'O']
]
'''
```