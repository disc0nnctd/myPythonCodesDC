s=" "
e="\n"
d="-"*80
prnt=s*35 + "SALARY REGISTER" + e + d + e
l=["S.No.","Name","Basic","HRA","Total","PF","Net-pay"]
prnt+="S.No." + s +"Name" + s*10 + "Basic" + s*5 + "DA" + s*8 + "HRA" + s*7 + "Total" + s*5 + "PF"+ s*8 + "Net-pay" 
prnt+=e + d + e
for i in range(1,6):
    nam=raw_input("Name: ")
    bas=input("Basic Salary: ")
    sno=i
    da=0.3*bas
    hra=0.1*bas
    tot=da+hra
    pf=0.1*(bas+da)
    net=tot-pf
    Sno=str(sno)
    if len(Sno)<6:
        Sno+=s*(6-len(Sno))
    name=nam
    if len(nam)<14:
        name+=s*(14-len(nam))
    basic=str(bas)
    if len(basic)<10:
        basic+=s*(10-len(basic))
    DA=str(da)
    if len(DA)<10:
        DA+=s*(10-len(DA))
    HRA=str(hra)
    if len(HRA)<10:
        HRA+=s*(10-len(HRA))
    Total=str(tot)
    if len(Total)<10:
        Total+=s*(10-len(Total))
    PF=str(pf)
    if len(PF)<10:
        PF+=s*(10-len(PF))
    prnt+=Sno + name + basic + DA + HRA + Total + PF + str(net)+ e
prnt+=d
with file("EMP.TXT","w") as f:
    f.write(str(prnt))
q=open("EMP.TXT","r")
p=q.read()
print p
