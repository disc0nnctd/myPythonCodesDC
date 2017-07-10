class Student:
    def __init__(self):
        self.name=""
        self.rno=0
        self.marks=()
        self.perc=0
        self.stream=""
    def inp(self):
        self.name=raw_input("Enter your name")
        self.rno=input("Enter Roll No.")
        subs=("English","P","C","M","CS")
        for i in subs:
            a=input("Enter marks in %s"%(i))
            self.marks+=(a,)
    def calc(self):
        self.perc=sum(self.marks)*0.2
        perc=int(self.perc)
        d={"(96,101)":"Computer Science","(91,96)":"Electronics",
           "(86,91)":"Mechanical","(81,86)":"Electrical",
           "(76,80)":"Chemical","(71,76)":"Civil"}
        for i in d.keys():
            r=eval(i)
            if perc in range(*r):
                self.stream=d[i]
    def display(self):
        self.calc()
        print "Name:%s\nRNo.:%s\nPercentage:%s\nStream:%s"%(self.name, self.rno, self.perc, self.stream)
        
x=Student()
x.inp()
x.display()
