# Create a class called Reptile that inherits from Animal in animal.py
# How do we make the Animal class a parent class?

from animal import Animal # Correct syntax for importing classes from another file - Note the capitalisation of the class to avoid confusion with the file

class Reptile(Animal): # Inherit from the Animal class
    def __int__(self):
        super().__init__() # super is used to inherit everything from the parent class - at the time of initialision
        self.cold_blooded = bool
        self.tetrapod = bool
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return ("Seeking the heat")
    def hunt(self):
        return("Working hard to find food!")
    def use_venom(self):
        return("If I have it I will use it!")

smart_reptile = Reptile()

# print(smart_reptile.hunt()) # New method only Reptiles can use
# print(smart_reptile.breathe()) # Inherited method from animal, can still use it :)





