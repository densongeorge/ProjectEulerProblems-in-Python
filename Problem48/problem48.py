###problem48=self powers

import math
import time
sum1=0
start=time.time()
for i in xrange(1,1001,1):
	e=0
	number1=1
	exp=i
	modulo=10000000000
        #calculates the power
	while(e<exp):
		number1=number1*exp
		number1=number1%modulo
		
		e=e+1
		
        sum1=(sum1+number1)%modulo
       # print i
        #print("number="+repr(number1))
        #print("e="+repr(e))
        #print("sum="+repr(sum1))
end=time.time()
print sum1
print end-start
                        
 
