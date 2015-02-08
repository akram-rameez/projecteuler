# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

qstn=600851475143
fmax = int(math.sqrt(qstn))

for x in xrange(fmax,1,-1):
	pass
	print x
	flag=0
	for y in xrange(int(math.sqrt(x)),1,-1):
		pass
		if x%y==0:
			pass
			flag+=1
			break
	if flag==0:
		pass
		if qstn%x==0:
			pass
			break

print x