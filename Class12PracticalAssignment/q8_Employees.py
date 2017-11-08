s=" "
e="\n"
d="-"*90
with file("EMP.TXT","w") as f:
    for i in range(1,6):
        sno=i
        nam=raw_input("Name: ")
        bas=input("Basic Salary: ")
        f.write(str(sno) + s + nam + s + str(bas)+"\n")

prnt=s*36 + "SALARY REGISTER" + e + d + e
prnt+="S.No." + s +"Name" + s*10 + "Basic" + s*7 + "DA" + s*10 + "HRA" + s*9 + "Total" + s*7 + "PF"+ s*10 + "Net-pay"
prnt+=e + d + e
q=open("EMP.TXT","r")
p=q.readline().split()
while p:
    sno=p[0]
    nam=p[1]
    bas=float(p[2])
    da=0.3*bas
    hra=0.1*bas
    tot=da+hra
    pf=0.1*(bas+da)
    net=tot-pf
    Sno=sno
    if len(Sno)<6:
        Sno+=s*(6-len(Sno))
    name=nam
    if len(nam)<14:
        name+=s*(14-len(nam))
    basic=str(bas)
    DA=str(da)
    HRA=str(hra)
    Total=str(tot)
    PF=str(pf)
    List=[basic,DA,HRA,Total,PF]
    for x in range(5):
        if len(List[x])<12:
            List[x]+=s*(12-len(List[x]))
        
    prnt+=Sno + name + List[0] + List[1] + List[2] + List[3] + List[4] + str(net)+ e
    p=q.readline().split()
q.close()
print prnt
