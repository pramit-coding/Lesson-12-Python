class Person (object):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

class Employee(Person):
    def __init__(self, name, age, type, id):
        self.type = type
        self.age = age

        Person.__init__(self, name, id)

a = Employee('Pramit', 15, 'Batsmen', 10)

a.display()




            