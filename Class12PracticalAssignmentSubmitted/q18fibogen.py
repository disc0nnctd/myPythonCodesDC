def fib(limit):
    a=0
    b=1
    if limit>10:
        print "Max 10 terms!"
        limit=10
    for _ in range(limit):
        yield a
        a,b=b,a+b
for i in fib(100):
    print i
