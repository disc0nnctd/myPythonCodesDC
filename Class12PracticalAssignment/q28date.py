#Perfect working isn't confirmed.
class DATE:
    def __init__(self):
        self.date=""
    def INPUT_DATE(self):
        self.date=raw_input("dd mm yyyy")
    def ADD_DAYS(self):
        d=self.date.split()
        p=int(d[0])
        q=int(d[1])
        r=int(d[2])
        p+=10
        leap=False
        if p>30 or q>12:
            while not (p<31 and q<12):
                if q%2==0 and q<>8 and q<>2:
                    while p>30:
                        p-=30
                        q+=1
                elif q%2<>0 or q==8 and q<>2:
                    while p>31:
                        p-=31
                        q+=1
                elif q==2 and not leap:
                    if not leap:
                        p-=28
                    else:
                        p-=29
                if q>12:
                    while q>12:
                        q-=12
                        r+=1
                if (r%4==0 or r%400==0) and r%100<>0:
                    leap=True
        self.date=str(p)+" "+str(q)+" "+str(r)
    def DISP_DATE(self):
        print self.date
n=DATE()
n.INPUT_DATE()
n.ADD_DAYS()
n.DISP_DATE()
