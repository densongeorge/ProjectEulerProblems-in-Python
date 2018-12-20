import math
import time
import sys


sys.stdout=open("problem50.txt",'w')

n=1000
booleanFlag=[1]*(n+1)
start=time.time()


for i in xrange(2,int(math.sqrt(n))+1) :
        if(booleanFlag[i]==1):
           for j in xrange(i**2,n+1,i):
               booleanFlag[j]=0

primes=[2]
for i in xrange(3,n+1):
    if(booleanFlag[i]==1):
        primes.append(i)



primescopy=list(primes)
#######################################################################################3
def sum(primes):
        sum=0        
        for i in primes:
                sum=sum+i
        return sum
def binsearch(primes, key, low = 0, high = len(primes) - 1):
    # bisecting the range
    while low < high:
        mid = (low + high)//2
        if primes[mid] < key:
            low = mid + 1
        else:
            high = mid
    # at this point 'low' should point at the place
    # where the value of 'key' is possibly stored.
    return low if primes[low] == key else 0        






###########################################################################################
tempsum=sum(primescopy)
#print tempsum

#print sum(primescopy[1:])
l=0

#print primescopy

numoftermsl=numoftermsr=numoftermseq=numofterms=maxsum=0
for l in xrange(0,n+1,1):
        
        r=n
        while(l<r):
                low=l
                high=r
##                leftsum=sum(primescopy[low:])
##                #print leftsum
##                if(binsearch(primescopy,leftsum)):
##                        numoftermsl=len(primescopy[low:])
##                        #print "hi"
##                rightsum=sum(primescopy[:high])
##               
##                        
##                if(binsearch(primescopy,rightsum)):
##                        numoftermsr=len(primescopy[:high])
                eqsum=sum(primescopy[low:high])
                #print eqsum
                if(binsearch(primescopy,eqsum)):
                        numoftermseq=len(primescopy[low:high])
##                if(numoftermsl>=numoftermsr and numoftermsl>numofterms and leftsum>maxsum):
##                        numofterms=numoftermsl
##                        maxsum=leftsum
##                      
##                if(numoftermsr>=numoftermsl and numoftermsr>numofterms and rightsum>maxsum):
##                        numofterms=numoftermsr
##                        maxsum=rightsum
                
                if(numofterms<numoftermseq and maxsum<eqsum):
                       numofterms=numoftermseq
                       maxsum=eqsum
                #print numofterms
                #print maxsum
                r=r-1


print maxsum
print numofterms
                
        

        
        

        



#print(primes)





end=time.time()

print end-start
