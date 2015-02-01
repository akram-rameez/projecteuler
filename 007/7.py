# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

import math

start=2
prime=[]

number=start

while len(prime)<10001:
	pass
	flag=0
	for x in xrange(2,int(math.sqrt(number))+1):
		pass
		if number%x==0:
			flag=1
	if flag==0:
		pass
		prime.append(number)
	number+=1

print "-->",prime[len(prime)-1]