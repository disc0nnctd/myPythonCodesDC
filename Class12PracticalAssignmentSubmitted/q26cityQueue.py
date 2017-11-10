q=[]
s=True
while s:
    print "1. Add   2. Delete    3. View    4.   Exit"
    a=input("input: ")
    if a==1:
        p=raw_input("You chose to add.\nEnter city: ")
        q.insert(0,p)
    if a==2:
        print "Dequeuing"
        q.pop()
    if a==3:
        print "Viewing the queue"
        print q
    if a==4:
        print "Exiting"
        s=False
