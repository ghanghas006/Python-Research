#parent class
class Pet():
    # class-level annotations
    name: None
    age: None
    species: None

    # constructor
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        


    def display(self):
        print("==========PET===========")
        print("Name:", self.name)
        print("Age: ", self.age)
        print("Species: ", self.species)

# Child Classes
class Cow(Pet):
    def sound(self):
        print("Moo!")
    def display(self):
        self.age += 1
        print("=====Cow======")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print(f"Happy Birthday '{self.name}'. Now you are '{self.age}'.")

class PolarBear(Pet):
    def sound(self):
        print("Chuffing!")
    def display(self):
        self.age += 1
        print("======Polar Bear======")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print(f"Happy Birthday '{self.name}'. Now you are '{self.age}'.")

class Chimpanzee(Pet):
    def sound(self):
        print("Pant-hoot!")
    def display(self):
        self.age += 1
        print("=====Chimpanzee=======")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print(f"Happy Birthday '{self.name}'. Now you are '{self.age}'. ")

class Lion(Pet):
    def sound(self):
        print("Hiss!")
    def display(self):
        self.age += 1
        print("=======Lion=========")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print(f"Happy Birthday '{self.name}'. Now you are '{self.age}'. ")
