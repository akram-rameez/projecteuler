# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

import math

count,ctr,n=0,0,0

def factors_sum(n):
	pass
	sum=1
	print 1,
	for x in xrange(2,int(math.sqrt(n))+1):
		if n%x==0:
			pass
			sum+=x+(n/x)
			if x==int(math.sqrt(n)):
				print x
			else:
				print x,(n/x),
	print " "
	return sum

ans=0

for x in xrange(2,10000):
	print "-->",x
	x1=factors_sum(x)
	x2=factors_sum(x1)

	if x1==x2:
		ans+=x1

print ans