import math
import time
#import collections
import sys


num=60085147 
n=int(math.sqrt(num))+1
#n=13195 
booleanFlag=(1*(n+1))



sys.stdout=open("problem7.txt",'w')

#sieve of eratosthenes for prime numbers
start=time.time()
for i in xrange(2,int(math.sqrt(num))+1) :
        if(booleanFlag[i]==1):
           for j in xrange(i**2,n+1,i):
               booleanFlag[j]=0

count=0
for i in xrange(2,num) :
    if(booleanFlag[i]==1):
        count=count+1
    if(count==101):
        print i
        break

        
