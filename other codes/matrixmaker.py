#making a matrix and saving inputs into a list
def mtx(m,n):
    a=[[0 for i in range(n)]for j in range(m)]
    l=[]
    for i in range(m):
        for j in range(n):
            s=a[i][j]=int(raw_input("Fill"))
            l.append(s)
    for i in range(m):
        for j in range(n):
            print a[i][j], '\t',
        print
    return l
print "Matrix 1"
m1=int(raw_input("Rows"))
n1=int(raw_input("Col"))
l1=mtx(m1,n1)