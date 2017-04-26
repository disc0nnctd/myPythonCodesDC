#count pallindromes in a sentence
def pal(word):
    return word == word[::-1]

s= raw_input("Enter a sentence: ").split()

c = 0
for w in s:
    if pal(w):
        c+= 1
    else:
        break
print " There are %s palindromes in your sentence\n."%(c)
