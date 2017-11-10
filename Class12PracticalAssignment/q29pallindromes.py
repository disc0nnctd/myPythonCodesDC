def writer():
    a=open("Words.txt","w")
    b=input("How many words to input? ")
    for i in range(b):
        c=raw_input("Word %s: "%(i+1))
        a.write(c+"\n")
    a.close()
def pal(x):
    if x[::-1]==x:
        return True
    else:
        return False
def list_pallindrome():
    a=open("Words.txt","r")
    b=a.readlines()
    l=[]
    for i in b:
        l.append(i[:-1])
    for j in l:
        if pal(j):
            print j
writer()
list_pallindrome()
