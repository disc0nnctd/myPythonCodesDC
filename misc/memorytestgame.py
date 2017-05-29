#
#DO NOT RUN IN PYTHON SHELL
#THIS PROGRAM IS STILL UNDER CONSTRUCTION
import os
def game():
    import time
    from random import randint
    w=True
    n=1
    while w:
        s=10**(n-1)
        e=(10**n)-1
        q=randint(s,e)
        i=5
        while i>0:
            print "Level",n
            print q," "*10,"Seconds remaining:",i
            time.sleep(1)
            i-=1
            os.system("cls")
        os.system("cls")
        p=int(raw_input("What number was that?\n Your input: "))
        if p==q:
            print "Match!"
            print "Proceeding to lvl 2"
            os.system("pause")
            os.system("cls")
            n+=1
##        elif p=='':
##            print "What? You can't simply press enter!"
##            n=1
##            os.system("pause")
        else:
            print "You lost! Resetting, the number was",q
            print "Resetting"
            n=1
            os.system("pause")

a=raw_input("press enter to begin")
if a=="":
    print "And the game begins \n You'll see a number for 5 seconds"
    os.system("pause")
    os.system("cls")
    game()
