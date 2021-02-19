## Basic I/O

Here we shall read about basic I/O functionalities in python. (I/O stands for Input/Output)\
Firstly, we will see how to print something in python. For this we have the print() function.

```python
print("Hello world!")
```

To make the print() function ignore some character, we can use '\'. Also, we use '\n' for newline and '\t' for getting a tab.

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

## Strings

## Sequences