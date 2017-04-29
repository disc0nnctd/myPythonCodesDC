"""A prgram that does Bubble Sort."""


def bubble(l):
    for j in range(len(l)-1, 0, -1):
        for i in range(j):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                # 'print l' in the loop will show the whole process
    print l


l = []
for p in range(10):
    print "Number ", p+1
    a = input("enter number ")
    l.append(a)
bubble(l)
