"""Swap object even position with the following odd position.

A function that takes a list and
its size as arguements and swaps the elements of every even location
with its following odd location.

However, if the number of elements in the list is odd, the last element will be ignored.
"""

def swapeo(l, size):
    """"The function that swaps."""
    if size%2== 0:
        rnge= size
    else:
        rnge= size-1
    for i in range(0 ,rnge, 2): #skips 2 steps
        l[i], l[i+1]=l[i+1], l[i] #swaps elements

l = input("Enter List")
size = len(l)
swapeo(l, size)
print l
l1 = input("Enter List")
size1 = len(l1)
swapeo(l1, size1)
print l1
