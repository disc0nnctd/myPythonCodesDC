"""Converts decimal to hexadecimal using dictionaries."""


hexa = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
a = input("enter decimal")
q = a
s = ''
while q > 0:
    r = q % 16
    q = q/16
    s += hexa[r]
    f = s[::-1]
