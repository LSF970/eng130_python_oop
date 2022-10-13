# Lucky draw
# keyword -> import

# import random
# Can also use:
# from random import *
# changes syntax for use though
# import math


# print(random) # Just shows where the imported file is
# print(random()) # Gives a completely random number 0 - 1

# Calculate DOB or year of birth

# from random import *
# import math
# import os
# import datetime, sys # You can use ',' to import multiple libraries
#
# # Using the math library
# number = 23.66
# # any numbers - to round figure up -
# # number 1.50 above round up = 2, 1.49 down round down = 1
#
# print(math.ceil(number)) # Rounds up to the nearest whole number - so even if number = 23.01 it will output 24
# print(math.floor(number)) # Round down to the nearest whole number - so even if number = 23.99 it will output 23
#
# # Using os, sys and datetime library
# print(os.cpu_count()) # Prints out how many cpu's your machine has
# print(datetime.date.today()) # Prints today's date depending on your OS
# print(sys.path) # Prints the current path the file is within

# Don't repeat yourself (DRY)
# reusable - saves time - saves money
# Let's build some functions
# It's part of your exam
# Syntax = def name(): -

# # First iteration
# def greeting():
#     # pass # - keyword to create a skeleton with no functionality
#     print("Hello, nice to meet you")
#
# greeting() # function can now be called whenever, without needing to write out the logic every time

# # Second iteration - greet the user with their name
# def greet_user(name): # Create a function that takes an argument - the name
#     print("Hello " + name)
#
# greet_user(input("Please enter your name")) # Asks user for name and then runs the function

# Function that takes int as an arg
def add(num1, num2): # Take user input as int and add them together, display outcome
    # print(num1 + num2)
    print("This function provides addition functionality") # Line shows that a print statement in the function runs also
# return statement
    return num1 + num2
# if you are using a return statement and calling the function, it needs to be in a print statement:
print(add(2, 2)) # When the function is called the args must be fulfilled

print(add(2321, 2324)) # Shows DRY - we can now reuse the function as many times as we like, with new args






