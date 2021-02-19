# Basics

Some basic concepts in python that you should know before starting basic programming.
Topics we will cover here:

1. Variables and Data types
2. Operators
3. Basic I/O
4. Strings
5. Lists
6. Tuples and Dictionaries

## Variables and Data types

In python you don't need to declare a variable. You can directly assign a value to a variable to declare it. 

```python
a = 3           # integer
text = "abcd"   # string
x = 6.9         # float (i.e. decimal numbers)
```

Data Types don't need to be explicity defined by the user. During *run-time* itself, variables get their data type from the data type of the value assigned to them. However, you *cannot* assign a value of a different data type to this variable once it has been assigned this data type.
These facts are summarised in two simple terms: Python is a *Dynamic* and a *Strongly-typed* language.

**Statically-typed**: Means that the data type is assigned at the very moment when the program is *compiled* (which happens before run-time). Examples: C, C++

**Dynamically-typed**: Means that the data type of the variable is assigned to it during *Run-time*. Examples: Python, JavaScript, PHP

There is no precise technical definition to strong and weak typing, but in general they refer to the following ideas

**Strongly-typed**: Means that the language has stricter typing rules, and hence there is a greater chance of getting errors or exceptions during compilation/run-time. Examples: Python, C#, Java.

**Weakly-typed**: Means that the language has weaker typing rules (in other words, it is somewhat "loosely typed"). There is more freedom and less chance of getting typing related errors. But the downside of this is unexpected behaviour of *flawed code* (because the language allows it to run, whereas a strongly typed language would never have let it run). Examples: JavaScript, PHP, C.

Some common features of strongly-typed languages are:

1. Explicit type definition to variables (To have to specify the type of a variable at the time of declaration). This is not followed by python (although python is called strongly typed due to other features). Also, even though C *does* follow this, it is instead usually considered weakly-typed (due to other features of the language). 
Some C code showing explicit type-definitions:

```C
int a;
char c = 'z';
float m = 0.98;
FILE *f = fopen("random_file.txt", "w");
```

2. Harder to perform type-conversions. It is difficult to convert data stored in one data type into another data type. (Conversion is usually assisted through type-casting).
3. There is usually no feature of using pointers in strongly-typed languages (because pointers could allow you to bypass the type-checking through pointer arithmetic).
