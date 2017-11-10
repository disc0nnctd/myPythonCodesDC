"""demonstrating single inheritance using a superclass and a subclass."""


class STUDENT(object):
    def __init__(self):
        self.name = raw_input("Name: ")
        self.house = raw_input("House: ")

class MARKS(STUDENT):
    def __init__(self):
        STUDENT.__init__(self)
        self.eng = input("English: ")
        self.phys = input("Physics: ")
        self.chem = input("Chemistry: ")
        self.maths = input("Maths: ")
        self.cs = input("CS: ")


stu = MARKS()
