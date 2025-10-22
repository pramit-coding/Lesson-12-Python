from abc import ABC

class square (ABC):
    def move(self):
        print("Hi am a square and I have multiple families ")

class rectangle(square):
    def move (self):
        print("Hi i am a rectange")

class quadrilateral(square):
    def move(self):
        print("Hi i am a quadreilateral")

class rombus(square):
    def move(self):
        print("Hi I am a rombus")
   

class parrelelogram(square):
    def move(self):
        print("Hi I am a parelelogram")

A = rectangle()
A.move()

B = quadrilateral()
B.move()

C = rombus()
C.move()

D = parrelelogram()
D.move()

print("This is some of the shapes in the family of 4 sided shapes")


