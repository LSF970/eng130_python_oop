# Create a class called Animal - File name starts with a - class name starts with A
# Add the common attributes/var behaviour and functions
# Syntax = class name: - class Animal:

class Animal: # follow the correct naming convention and best practices
    # we need to initialise the class with built-in method __init__(self)
    # self refers to current class
        def __init__(self): # any attributes attached to the class should be part of the __init__ method
            # self.var = True - as an example
            self.alive = True
            self.spine = True
            self.eyes = True
            self.lungs = True

# let's create some methods to add common behaviours
        def breathe(self):
            return "Breathe in, Breathe out"
        # One more behaviour
        def eat(self):
            return "NOM, NOM, NOM"

# Create an object of this class - Instantiate - The Animal is theoretical or just a blueprint
cat = Animal() # creating an object of the Animal class

# print(cat.breathe()) # calling a method using object of the Animal class
# print(cat.eat())










