# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

sum=0

def is_prime(n):
	for x in xrange(2,int(math.sqrt(n))+1):
		pass
		if n%x==0:
			pass
			return False
			break
	return True

for x in xrange(2,2000000):
	pass
	if is_prime(x):
		pass
		sum+=x

print sum