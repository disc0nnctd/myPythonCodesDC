d="-"
preprnt=d*80 + "\n"
preprnt+="Name of the student" + " " + "House" + " "*3 + "Amount collected" + "\n" + d*80 + "\n"
prnt=preprnt
for i in range(1):
    nam=raw_input("Name: ")
    hou=raw_input("House: ")
    amt=raw_input("Amount Collected: ")
    name=nam
    if len(nam)<20:
        name+=" "*(20-len(nam))
    house=hou
    if len(hou)<8:
        house+=" "*(20-len(hou))
    prnt+= name+house+amt+"\n"
prnt+=d*80
with file("Student.txt","w") as stu:
    stu.write(prnt)
q=open("Student.txt","r")
p=raw_input("Enter house: ")
r=q.readlines()

print preprnt,
for j in r:
    if p in j:
        print j,
print d*80
