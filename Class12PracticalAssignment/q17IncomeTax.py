class Tax:
    def __init__(self,name,income):
        self.name=name
        self.income=income
        self.tax=0
    def IncomeTax(self):
        x=self.income
        if x <= 3500:
            self.tax=0
        elif x in range(3501,60001):
            self.tax=0.2*x
        elif x in range(60001,120001):
            self.tax=0.3*x
        elif x>12000:
            self.tax=0.4*x
    def Print(self):
        print "Name: ", self.name
        print "Income: ", self.income
        self.IncomeTax()
        print "Tax: ", self.tax
s=Tax("Name",200000)
s.Print()
