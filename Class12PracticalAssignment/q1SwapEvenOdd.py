"""Swap object on even position with the following odd position.

A function that takes a list and
its size as arguements and swaps the elements of every even location
with its following odd location.

However, if the number of elements in the list is odd, the last element will be ignored.
"""

def swapeo(l, size):
    """"The function that swaps."""
    if len(l)%2==0:
        rnge=len(l)
    else:
        rnge=len(l)-1
    for i in range(0,rnge,2):
        l[i], l[i+1]=l[i+1], l[i]

l = input("Enter List")
size = len(l)
swapeo(l, size)
print l
