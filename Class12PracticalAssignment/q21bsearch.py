array=[]
def input_data(n):
    global array
    for i in range(n):
        s=input(("Enter number %s: ")%(i+1))
        array.append(s)
    array=sorted(array)
def Bsearch(target):
    global array
    array=sorted(array)
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) / 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x
input_data(10)
