# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def valid(a,b,c):
	pass
	if (a+b)>c:
		pass
		if(a+c)>b:
			pass
			if (b+c)>a:
				pass
				if a+b+c==1000:
					pass
					return True
	return False

while sum!=0:
	pass
	for x in xrange(3,1000):
		pass
		for y in xrange(x,1000):
			pass
			for z in xrange(y,1000):
				pass
				if valid(x,y,z):
					pass
					if(x**2+y**2)==z**2:
						print x,y,z
						print x*y*z
