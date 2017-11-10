import pickle
a=open("stud.dat","wb")#This is for writing, not a part of question
for i in range(5):
    s=raw_input("Name")
    t=raw_input("Class")
    u=raw_input("Cat(BSP/NBSP)")
    v=raw_input("Sex")
    pickle.dump((s+" "+t+" "+u+" "+v), a)

##program starts here###

d="-"*45
prnt=d+"\n"
T=("Name"+" "*16,"class  ","Cat(BSP/NBSP)  ","Sex")
for i in T:
    prnt+=i
prnt+="\n" + d + "\n"
a=open("stud.dat","rb")
s=pickle.load(a).split()
bsp=0
nbsp=0
boy=0
girl=0
try:
    while s:
        nam=s[0]
        cls=s[1]
        cat=s[2]
        sex=s[3]
        if cat=="BSP":
            bsp+=1
        else:
            nbsp+=1
        if sex=="M":
            boy+=1
        else:
            girl+=1
        L=[nam,cls,cat]
        for i in range(3):
            if len(L[i])<len(T[i]):
                L[i]+=" "*(len(T[i])-len(L[i]))
                prnt+=L[i]
        prnt+=sex + "\n"
        s=pickle.load(a).split()
except EOFError:
    pass
prnt+=d + "\n"
prnt+="Total BSP: %s\nTotal NBSP: %s\nTotal Boys: %s\nTotal Girls: %s"%(bsp, nbsp, boy, girl)
prnt+="\n" + d
print prnt
