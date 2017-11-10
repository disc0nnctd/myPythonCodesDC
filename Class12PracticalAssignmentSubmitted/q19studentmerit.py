stud={}
for i in range(10):
    a, b=raw_input("Name <space> R.No: "), input("Percentage: ")
    stud[a]=b
with open("Result.txt","w") as w: w.write(str(stud))
with open("Result.txt","r") as q: stud=eval(q.read())  #converts the string "{}" into dictionary
st,prnt={},""
for i in stud.keys():  #creates a reversed dictionary with percentage as keys
    if stud[i] in st: st[stud[i]]+=[i]
    else: st[stud[i]]=[i]
T=("Rank ","R.No. ","Name"+" "*6,"Percentage")
for o in T: prnt+=o
prnt+="\n"
e=sorted(st.keys())[::-1]
for a in range(len(e)):  
    for p in sorted(st[e[a]]):  #sorted arranges names alphabetically
        name, rno=p.split()[0], p.split()[1]
        rank, perc=str(a+1), str(e[a])
        L=[rank,rno,name,perc]
        for i in range(3):
            if len(L[i])<len(T[i]): L[i]+=" "*(len(T[i])-len(L[i]))
        prnt+=L[0]+L[1]+L[2]+L[3]+"\n"
print prnt
