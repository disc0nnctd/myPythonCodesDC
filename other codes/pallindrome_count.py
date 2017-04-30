"""Counts pallindromes in a sentence."""


def pal(word):
    return word == word[::-1]


s = raw_input("Enter a sentence: ").split()
c = 0
l = []
for w in s:
    if pal(w):
        c += 1
        l.append(w)
    else:
        break
print " There are %s palindromes in your sentence." % (c)
print "The following list shows the pallindromes in your sentence: \n", l
