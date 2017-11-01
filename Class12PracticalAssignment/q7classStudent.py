class student(object):
    def __init__(self):
        self.rollno=0
        self.name=""
    def Getdata(self):
        self.rollno=input("Roll no.: ")
        self.name=raw_input("Name: ")
    def Printdata(self):
        print "Roll no.: %s\nName: %s" % (self.rollno, self.name)
class marks(student):
    def __init__(self):
        self.sub1=0
        self.sub2=0
        self.sub3=0
        self.sub4=0
        self.sub5=0
    def Inputdata(self):
        self.sub1=input("Sub1: ")
        self.sub2=input("Sub2: ")
        self.sub3=input("Sub3: ")
        self.sub4=input("Sub4: ")
        self.sub5=input("Sub5: ")
    def Outdata(self):
        super(marks,self).Printdata()
        print "Sub1: %s\nSub2: %s\nSub3: %s\nSub4: %s\nSub5: %s"%(self.sub1, self.sub2, self.sub3, self.sub4, self.sub5)
s=marks()
s.Getdata()
s.Inputdata()s
s.Outdata()
