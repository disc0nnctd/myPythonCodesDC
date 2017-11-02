t=()
i=0
while i<5:
    user=raw_input("Enter username: ")
    if user in t:
        print "user already exists"
        pass
    else:
        password=raw_input("password: ")
        i+=1
        t+=(user,password)
def login():
    global auth
    print "ENTER LOGIN DETAILS"
    user=raw_input("username: ")
    auth=False
    if user in t:
        for i in range(len(t)):
            if t[i]==user:
                password=raw_input("password: ")
                if password==t[i+1]:
                    print "access allowed"
                    auth=True
                else:
                    print "wrong password"
    else:
        print "username not found"
auth=False
while not auth:
    login()
