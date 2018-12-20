#!/usr/bin/python
def primenumber(num):
	flag=1
	primelimit=(num//2)+1
	for i in range(2,primelimit):
		#print "primelimit:"
		#print primelimit
		if (num%i!=0 and num!=i):
			continue
			
		else:
			flag=0
			break
		
	if (flag==1):
	#	print num
		return 1;
	else :
		return 0
sum=0;
for i in range(2,2000000):
	if(primenumber(i)):
		sum=sum+i
print sum
   
  

	
			
	
		