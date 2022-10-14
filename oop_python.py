from snake import Snake

class Python(Snake):

    def __int__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False


    def digest_large_prey(self):
        return "No matter how big you are, I can eat you!"
    def constrict_large_prey(self):
        return "I'm going to squeeze you!"
    def climb(self):
        return "Going up!"
    def shed_skin(self):
        return "I'm not comfortable in the skin I am in. Lets change that"

billy_the_python = Python()

print(billy_the_python.shed_skin()) # Method only available to Python class
print(billy_the_python.use_tongue_to_smell()) # Inherited method from Snake class
print(billy_the_python.hunt()) # Inherited method available to Reptile objects
print(billy_the_python.eat()) # Inherited method available to Animal objects

# We now have four tiers of Inheritence:  Animal -> Reptile -> Snake -> Python