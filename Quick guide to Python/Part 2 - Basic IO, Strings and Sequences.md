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
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

You can obtain either single characters, or groups of characters from a string by performing indexing or slicing operations respectively:

```py
name = "Rachit"

print(name[0]) # Indexing. Output will be: R
print(name[4]) # Indexing. Output will be: i
print(name[-1]) # Again indexing. Output will be: t

print(name[0:3]) # Slicing. Output will be: Rac
print(name[0:1]) # Slicing. Output will be: R
print(name[0:5]) # Slicing. Output will be: Rachi
print(name[2:4]) # Slicing. Output will be: ch
print(name[3:5]) # Slicing. Output will be: hi
print(name[-4:-1]) # Slicing. Output will be: chi
print(name[0:]) # Slicing. Output will be: Rachit
print(name[:]) # Slicing. Output will be: Rachit
```

From the above examples of slicing, you must have noticed that when performing slicing, the first index is *included* but the second (closing) index is *excluded*. For example, ```[2:5]``` would mean indexes 2, 3 and 4.

## Sequences