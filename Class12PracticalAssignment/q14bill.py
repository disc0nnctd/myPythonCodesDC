##Sample CGEB.txt
##Dan 094230 091787
##John 085000 084293
##Patrick 092777 092000
##Ben 094823 074120
##Oliver 095120 094330

d="-"*74
prnt=d+"\n"
T=("Consumer's name","Current_Reading","Prev_reading","Consumed_unit","Bill amount")
prnt+="%s  %s  %s  %s  %s"%(T[0],T[1],T[2],T[3],T[4])
prnt+="\n" + d + "\n"
a=open("CGEB.txt","r")
b=a.readline().split()
while b:
    name=b[0]
    cur=b[1]
    prev=b[2]
    con=int(cur)-int(prev)
    if con <= 100:
        bill=0.75*con
    elif con in range(101,201):
        bill=1.25*con
    elif con in range(201,301):
        bill=1.75*con
    else:
        bill=2.25*con
    con=str(con)
    L=[name,cur,prev,con]
    for i in range(4):
        if len(L[i])<len(T[i]):
            L[i]+=" "*((len(T[i])+2)-len(L[i]))
    prnt+=L[0]+L[1]+L[2]+L[3]+str(bill)+"\n"
    b=a.readline().split()
a.close()
prnt+=d
print prnt
