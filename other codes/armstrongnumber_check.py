#Checks if a number is an armstrong number
#if a number has n digits and
#the sum of the digits separately raised to nth power is equal to the number
#then it is called an Armstrong number
x=input("Enter any no. ")
y=x
lth=len(str(x)) # the power to which the digits have to be raised
sum=0
while y>0:
    j=y%10 #the remainder will be the last digit
    sum=sum+(j**lth)
    y=y/10 #the last digit will be removed
if sum==x:
    print "%s is an Armstrong number. " %(x)
else:
    print "%s is NOT an Armstrong number. "%(x)
