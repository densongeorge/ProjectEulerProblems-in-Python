#sieve of eratosthenes for prime numbers
n=1000000
booleanFlag=[1]*(n+1)

import math
import time
#import collections
import sys

#sys.stdout=open("Primenum.txt",'w')



def rotate(boollist,numb):
    flag=1
    rotateby=len(numb)
    for index in xrange(1,rotateby+1):
        rotatednumber=numb[index:]+numb[:index]
        #if(numb=="101"):
            
         #   print rotatednumber
        if(boollist[int(rotatednumber)]==0):
            flag=0
            break
    if(flag==1):
        boollist[int(numb)]=2



start=time.time()
for i in xrange(2,int(math.sqrt(n))+1) :
        if(booleanFlag[i]==1):
           for j in xrange(i**2,n+1,i):
               booleanFlag[j]=0


for i in range(2,n+1):
           if (booleanFlag[i]==1):
                #print i
                #break
                rotate(booleanFlag,str(i))

count =0
for i in range(2,n):
        if(booleanFlag[i]==2):
            #print i
            count=count+1
print count
           
end=time.time()
#print end-start

 
            
