# A program to store few sentences in a file SENT.txt and then print the number
# of 'to' and 'the' present in it
# take care that using 'a' or 'a+' will add to the file
# while 'w' or 'w+' will replace it
# using "with" ensures that the file will be closed without using .close()

with open("SENT.TXT", "w") as sent:  # for writing and creating a file
    while True:
        q = raw_input("Do you want to add more lines? Y/N: ")
        if q.upper() == "Y":
            a = raw_input("Enter a line: ")
            sent.write(a+"\n")
        else:
            break
with open("SENT.TXT", "r") as sent:  # for reading
    cts = sent.read()
strs = ["to", "the"]
for i in range(len(strs)):
        print "Number of '%s' in file is %s" % (strs[i], cts.count(strs[i]))
