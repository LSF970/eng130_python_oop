# Python Object-Oriented Programming
## The four pillars of OOP
#### Methods and Functions
#### Modules, Packages and Libraries

##### use case - benefits - examples of builtin modules - packages

## Importing libraries
Importing from libraries allows us to use vast range of functions and methods to do common tasks. To import a library present in our file structure:
```python
import random
# Can also use:
from random import *
```
## Using libraries in our code
#### math library 
```python
# # Using the math library
number = 23.66
# # any numbers - to round figure up -
# # number 1.50 above round up = 2, 1.49 down round down = 1

print(math.ceil(number)) 
# Rounds up to the nearest whole number - so even if number = 23.01 it will output 24
print(math.floor(number)) 
# Round down to the nearest whole number - so even if number = 23.99 it will output 23
```
#### os, sys and datetime libraries
```python
# # Using os, sys and datetime library

print(os.cpu_count()) 
# Prints out how many cpu's your machine has

print(datetime.date.today()) 
# Prints today's date depending on your OS

print(sys.path) 
# Prints the current path the file is within
```
## Making code reusable using functions
Remember one of the first things we told you when we started Python

DRY - Don't Repeat Yourself.

Making our code reusable is extremely important if we are to keep DRY in mind, remember DRY helps save time and money. We can do this by creating functions that hold the actions we may want to use again at various points of our program. Let's see how to build them.


The first iteration shows us how to make a really simple function. Even such a simple function saves us some time.
```python
# # First iteration
def greeting():
#     # pass # - keyword to create a skeleton with no functionality
      print("Hello, nice to meet you")

greeting() 
# function can now be called whenever, without needing to write out the logic every time
# Output is Hello, nice to meet you
# But can be called over and over again without needing to tyoe the whole print statement again.
```

The second iteration takes user input. Again nice and simple but showcases the power of funcitons.

```python
# # Second iteration - greet the user with their name
def greet_user(name): 
# Create a function that takes an argument - the name
      print("Hello " + name)

greet_user(input("Please enter your name"))
# Asks user for name and then runs the function
```
## Taking arguments
We can take away much of the 'hard coding' of values in a similar way to the input change from iteration from function 1 to funciton 2. The name part of `def greet_user(name):` is the argument in the above case. We must then fulfil this argument (arg) whenever we call the function.

The below example shows how this is best practice for two reasons.
1. it allows us to take values dynamically rather than hard coding them
2. it allows us to use `return` and thus remove unnecessary methods from function. They can instead be used when the function is called on an individual basis.

```python
# Function that takes int as an arg
def add(num1, num2): 
    # Take user input as int and add them together, display outcome
      print(num1 + num2)
      print("This function provides addition functionality") 
    # Above shows that a print statement in the function runs also
# return statement
      return num1 + num2
# if you are using a return statement and calling the function, it needs to be in a print statement:
print(add(2, 2)) 
# When the function is called the args must be fulfilled

print(add(2321, 2324)) 
# Shows DRY - we can now reuse the function as many times as we like, with new args

```
![](https://github.com/LSF970/eng130_python_oop/blob/main/images/OOP_Python.png)



