p=input("Enter first row: ")
q=input("Enter second row: ")
r=input("Enter third row: ")

r1=sum(p)
r2=sum(q)
r3=sum(r)
c1=p[0]+q[0]+r[0]
c2=p[1]+q[1]+r[1]
c3=p[2]+q[2]+r[2]
dia1=p[0]+q[1]+r[2]
dia2=p[2]+q[1]+r[0]

if r1==r2==r3==c1==c2==c3==dia1==dia2:
    print "It's a Magic Square."
else:
    print "Not a Magic Square."
