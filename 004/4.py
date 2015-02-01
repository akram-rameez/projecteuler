# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(n):
	pass
	string=str(n)

	if string==string[::-1]:
		pass
		return True

arr=[]

for x in xrange(999,0,-1):
	pass
	for y in xrange(999,0,-1):
		pass
		if palindrome(x*y):
			pass
			arr.append(x*y)

print max(arr)