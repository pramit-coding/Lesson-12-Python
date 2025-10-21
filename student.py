class Teacher:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def printname(self):
        print(self.first, self.last)

class Student(Teacher):
    def __init__(self, first, last, grade):
        self.grade = grade

        super().__init__(first,last)
        self.report = grade

a = Student("Pramit", "Panchal", 100)
a.printname()
print(a.report)