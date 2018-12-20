import math
import time
import sys


sys.stdout=open("problem2a.txt",'w')
start=time.time()



def fibusinggoldenratio():
    sum=0
    init=2
    goldr3=4.236068
    while(init<4000000):
        sum=sum+init
        
        init=int(round(init*goldr3))
     #   print init
        
    print sum

def fib():
    sum=0
    n=1000
    b=1
    c=1
##    for i in xrange(3,n+2,1):
##        fib.append(fib[i-1]+fib[i-2])
    while(n!=1):
        d=b+c
        b=c
        c=d
        if(d%2==0 and d<4000000):
            print d
            sum=sum+d
        n=n-1
    #print d
    #return fib
    print sum




#print fibo
##for i in fibo:
##    if (i%2==0):
##        sum=sum+i
##        
##print sum
fib()
fibusinggoldenratio()
end=time.time()
print end-start
