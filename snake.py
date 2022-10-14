from reptile import Reptile

class Snake(Reptile):

    def __int__(self):
        super().__init__()
        self.cold_blooded = True
        self.forked_tongue = True
        self.venom = bool
        self.limbs = False

    def use_tongue_to_smell(self):
        return "Pssst, I can smell you with my tongue"

adder = Snake()

# print(adder.use_tongue_to_smell()) # Method only available to Snake
# print(adder.hunt()) # Method available to Reptile objects
# print(adder.eat()) # Method available to Animal objects

# Add all of these into a fourth class and add this to documentation