"""Swap object on even position with the following odd position.

A function that takes a list and
its size as arguements and swaps the elements of every even location
with its following odd location
"""
# you'll have to call the function again to use it.


def swapeo(l, size):
    """"The function that swaps."""
    for i in range(size-1):
        pos = i+1
        if pos % 2 == 0:
            l[i], l[i+1] = l[i+1], l[i]
    return l


l = input("Enter List")
size = len(l)
swapeo(l, size)
print l
