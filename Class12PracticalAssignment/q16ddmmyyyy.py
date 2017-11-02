def date(s):
    dic={1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
       6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November",
       12:"December", "1":"1st","2":"2nd","3":"3rd"}
    l=s.split()
    dd=l[0]
    if l[0][-1] in dic:
        if len(dd)==1:
           dd=dic[dd]
        elif dd[0]=="1":
            dd+="th"
        else:
            dd=dd[0]+dic[dd[1]]
    else:
        dd+="th"
    mm=dic[int(l[1])]
    yyyy=l[2]
    print "%s %s %s" %(dd,mm,yyyy)

date("29 10 2017") #example: should give "29th October 2017"

s=raw_input("dd mm yyyy")
