# Program Logic and Error Handling

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

## While Loop

## Jump Statements

## Error Handling