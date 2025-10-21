from abc import ABC

class Animal(ABC):
    def move(self):
        pass


class Cub(Animal):
    def move(self):
        print("I am the Cub child of the Animal")

class Prey(Animal):
    def move(self):
        print("I am the prey of the Animal")

class Predator(Animal):
    def move(self):
        print("I am the Predator of the Animal")

class Habitat(Animal):
    def move(self):
        print("I am the lion's home :)")

W = Cub()
W.move()

S = Prey()
S.move()

A = Predator()
A.move()

D = Habitat()
D.move()


    

