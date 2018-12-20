#not working!!!

import math
import time
#import collections
import sys

n=20
num=20

#n=13195 
booleanFlag=[1]*(n+1)



sys.stdout=open("problem5.txt",'w')

#sieve of eratosthenes for prime numbers
start=time.time()
for i in xrange(2,int(math.sqrt(n))+1) :
        if(booleanFlag[i]==1):
           for j in xrange(i**2,n+1,i):
               booleanFlag[j]=0

#print booleanFlag
factors=[]
i=2
lcm=1
countoffactors={}
while(i<=num):
        if(booleanFlag[i]==1 and i>3):
                lcm=lcm*i
        i=i+1


print lcm      
primes=[]      
##for i in xrange(2,num):
count2=0
count3=0
maxcount2=0
maxcount3=0
i=2
for nomber in range(2,20):
        if(count2>maxcount2):
                maxcount2=count2
        if(count3>maxcount3):
                maxcount3=count3
        count2=0
        count3=0
        i=nomber
        while i>1 :
                if(i%2==0):
                        #primes.append(i)
                                #print i
                        i=i/2
                        count2=count2+1
                elif(i%3==0):
                        i=i/3
                        ##factors.append(i)
                        count3=count3+1
        print count2
        print count3
                        


##while
##        count=0
##        while(not factors):
##                number=factors[0]
##                if(number in primes):
##                        factors.remove(number)
##                        count=count+1
##                
##                
##                
## countoffactors[number]=countoffactors[number]+1       
        
end=time.time()
print end-start
