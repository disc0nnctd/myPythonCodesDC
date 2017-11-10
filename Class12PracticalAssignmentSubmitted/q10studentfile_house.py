with file("Student.txt","w") as stu:
    for i in range(5):
        nam=raw_input("Name: ")
        hou=raw_input("House: ")
        amt=raw_input("Amount Collected: ")
        stu.write(nam+" " + hou + " " + amt      + "\n")

d="-"
preprnt=d*80 + "\n"
preprnt+="Name of the student" + " " + "House" + " "*3 + "Amount collected" + "\n" + d*80 + "\n"
prnt=preprnt

q=open("Student.txt","r")
p=raw_input("Enter house: ")
r=q.readline().split()
while r:
    if r[1]==p:
        name=r[0]
        house=r[1]
        amt=r[2]
        if len(name)<20:
            name+=" "*(20-len(name))
        if len(house)<8:
            house+=" "*(8-len(house))
        prnt+= name + house + amt + "\n"
    r=q.readline().split()
q.close()
print prnt
print d*80
