# Question:

# You are tasked with modeling a zoo using object-oriented programming. Design a set of classes that represent different types of animals in the zoo.
# Start with a base class called Animal and create at least two subclasses, Mammal and Bird. Each subclass should have additional attributes and 
# methods specific to the type of animal. Additionally, create a class called Zoo that can contain various instances of animals.

# The Animal class should have attributes like name, age, and sound. It should have a method make_sound() that prints the sound the animal makes.

# The Mammal class should inherit from Animal and have an additional attribute fur_color. It should also have a method give_birth() that prints a
# message indicating that the mammal is giving birth.

# The Bird class should inherit from Animal and have an additional attribute wing_span. It should have a method fly() that prints a message indicating
# that the bird is flying.

# The Zoo class should have a method add_animal(animal) to add an animal to the zoo and a method make_sounds() that calls the make_sound() method for
# each animal in the zoo.

# Demonstrate the usage of these classes by creating instances of different animals, adding them to a zoo, and making them perform their specific 
# actions.

class Animal:
    def __init__(self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"name: {self.name} sound : {self.sound}")

class Mammal(Animal):
    def __init__(self, name, age, sound,fur_color):
        super().__init__(name, age, sound)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} mammal is giving birth")

class Bird(Animal):
    def __init__(self, name, age, sound,wing_span):
        super().__init__(name, age, sound)
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.name} bird is flying with a wing span of {self.wing_span}")

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self,animal):
        self.animals.append(animal)
    
    def make_sounds(self):
        for animal in self.animals:
            animal.make_sound()


zoo = Zoo()

tiger = Mammal('tiger',10,'roar','orange')
parrot = Bird('parrot',1,'trills',2)

zoo.add_animal(tiger)
zoo.add_animal(parrot)

zoo.make_sounds()
tiger.give_birth()
parrot.fly()

