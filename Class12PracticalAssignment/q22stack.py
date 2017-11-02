stack=[]
s=True
while s:
    print "1. Push   2. Pop    3. View    4.   Quit"
    a=input("input: ")
    if a==1:
        p=input("You chose to push.\nEnter number: ")
        stack.append(p)
    if a==2:
        print "Popping"
        stack.pop()
    if a==3:
        print "Viewing the stack"
        print stack
    if a==4:
        print "Quitting"
        s=False
