import math
import time
#import collections
import sys


num=999
#n=13195 

sys.stdout=open("problem4.txt",'w')

def isPalindrome(product):
	productinstr=str(product)
	if(productinstr==productinstr[::-1]):
		return True
	else:
		return False
		
palindrome=0
product=0
for i in range(999,100,-1):
	for j in range(999,100,-1):
			product=i*j
			if(isPalindrome(product)):
				if(product>palindrome):
					palindrome=product
print palindrome
				

	