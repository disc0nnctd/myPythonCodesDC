d={}
for i in range(5):
    a=raw_input("Country input: ")
    b=raw_input("Capital input: ")
    d[a]=b
with open("Quiz.dbf","w") as w:
    w.write(str(d))

m=open("Quiz.dbf","r")
d=eval(m.read())
s=raw_input("Country: ")
print "Captial: ", d[s]
m.close()
