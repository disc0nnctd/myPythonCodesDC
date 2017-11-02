stud={}
for i in range(5):
    a=raw_input("Name: ")
    b=input("Percentage: ")
    stud[a]=b
with open("Result.txt","w") as w:
    w.write(str(stud))
q=open("Result.txt","r")

stud=eval(q.read())  #converts the string "{}" into dictionary
q.close()
st={}
for i in stud.keys():  #creates a reversed dictionary with percentage as keys
    if stud[i] in st:
        st[stud[i]]+=[i]
    else:
        st[stud[i]]=[i]
e=sorted(st.keys())[::-1]
for a in range(len(e)):  
    for p in sorted(st[e[a]]):  #sorted arranges names alphabetically
        name=p
        print "%s. %s %s" %(a+1, name, e[a]) #Those with same percentage will share rank 
