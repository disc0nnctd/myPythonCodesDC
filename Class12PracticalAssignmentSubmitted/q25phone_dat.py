import pickle
d=open("Student.dat","wb")
for i in range(5):
    a=raw_input("Name: ")
    b=raw_input("Phone Number: ")
    pickle.dump(a+" "+b,d)
d.close()

try:
    s=open("Student.dat","rb")
    r=pickle.load(s)
    search=raw_input("Search Name: ")
    found=False
    while True:
        if search in r:
            print r
            r=pickle.load(s)
            found=True
        else:
            r=pickle.load(s)
except EOFError:
    pass

finally:
    if not found:
        print "NOT FOUND"
