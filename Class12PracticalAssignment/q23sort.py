def IS_SORT(lst):
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            sort=True
        else:
            sort=False
            break
    return sort
print IS_SORT([1,2,4,5])
print IS_SORT([1,5,2,3])
