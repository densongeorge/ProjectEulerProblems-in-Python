import math
import time
#import collections
import sys


num=600851475143 
n=int(math.sqrt(num))+1
#n=13195 
booleanFlag=[1]*(n+1)



sys.stdout=open("problem3.txt",'w')

#sieve of eratosthenes for prime numbers
start=time.time()
for i in xrange(2,int(math.sqrt(n))+1) :
        if(booleanFlag[i]==1):
           for j in xrange(i**2,n+1,i):
               booleanFlag[j]=0

factors=[]

for i in xrange(2,n):
	if(booleanFlag[i]==1):
		print i
		if(num%i==0):
			num=num/i
			factors.append(i)
if(not factors):
        factors.append(num)

print factors
end=time.time()
print end-start


			   

