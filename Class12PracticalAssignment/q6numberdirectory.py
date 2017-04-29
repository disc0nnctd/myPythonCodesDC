"""Writes and reads phone directory."""

"""A program to create data file and store name and phone numbers
Ask user to input name, display the phone number; else print 'not found'
"""
with open("STD.txt", "a") as std:  # writing
    d = {}
    r = 5  # number of names to be entered
    for i in range(r):  # takes dictionary
        a = raw_input("enter name")
        b = raw_input("enter phone number")
        if len(str(b)) != 10:
            b = raw_input("Please enter 10 digit number")
        d[a] = b
    print d
    std.write(str(d))

with open("STD.txt", "r") as std:  # reading
    d = eval(std.read())
    q = raw_input("Enter student name")
    if q in d:
        print "%s's phone number is %s" % (q, d[q])
    else:
        print "Not found in directory."
