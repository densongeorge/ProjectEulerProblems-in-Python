import math
import time
import sys


sys.stdout=open("problem47.txt",'w')

n=1000
booleanFlag=[1]*(n+1)
start=time.time()


for i in xrange(2,int(math.sqrt(n))+1) :
        if(booleanFlag[i]==1):
           for j in xrange(i**2,n+1,i):
               booleanFlag[j]=0

def numOfFactors(n,booleanFlag):
        factors=set( )
        i=2
        while(i<int(math.sqrt(n))+1):
                if (booleanFlag[i]==1):
                        if(n%i==0):
                           factors.add(i)
                           n=n//i
                           print n
                           i=2
                        else:
                           i=i+1
                           print i
        
        if(n>1):
                factors.add(n)
        #print repr(n) + "=" + str(factors)            
        print factors
        print n
        return len(factors)



##        for maxm in xrange(100,n+1):
##                temp=maxm
##                counter=3
##                expected=3
numboffacts=numOfFactors(100,booleanFlag)
print numboffacts
##                while(counter>0):
##                                temp=temp+1
##                                numboffacts=numOfFactors(temp,booleanFlag)
##                                if(expected==numboffacts):
##                                        counter=counter-1
##                                else :
##                                        break
##                if(expected==numboffacts):
##                        print maxm
##                        



