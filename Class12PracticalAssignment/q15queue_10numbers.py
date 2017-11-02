q=[]
for i in range(1,11):
    x=input(("Enter number %s: "%i))
    q.append(x)
s=True
while s:
    print "1. Add   2. Delete    3. View    4.   Quit"
    a=input("input: ")
    if a==1:
        p=input("You chose to add.\nEnter number: ")
        q.insert(0,p)
    if a==2:
        print "Dequeuing"
        q.pop()
    if a==3:
        print "Viewing the queue"
        print q
    if a==4:
        print "Quitting"
        s=False
