A=[]
for l in range(5):
    A.append(raw_input("Input: "))
for i in range(len(A)):
    mini= i
    for j in range(i+1, len(A)):
        if A[mini][0] > A[j][0]:
            mini = j
    A[i], A[mini] = A[mini], A[i]
    print A
