"""demonstrating single inheritance using a superclass and a subclass."""


class STUDENT:
    def __init__(self):
        self.name = raw_input("name")
        self.house = raw_input("house")

class MARKS(STUDENT):
    def __init__(self):
        STUDENT.__init__(self)
        self.eng = input("eng")
        self.phys = input("phys")
        self.chem = input("chem")
        self.maths = input("maths")
        self.cs = input("cs")


stu = MARKS()
