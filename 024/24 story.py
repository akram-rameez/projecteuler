# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# 0 123
# 0 132
# 0 213
# 0 231
# 0 312
# 0 321

# 1023
# 1032
# 1203
# 1230
# 1302
# 1320
# 2013
# 2
# 2
# 2
# 2
# 2
# 3
# 3
# 3
# 3
# 3
# 3

import math

digits = [0,1,2,3]
digits.sort()
print "Number of digits:",len(digits)
print "digits:",digits

n = 5

print "digits change in the place every",math.factorial(len(digits)-1),"numbers"
print "there are a total of",math.factorial(len(digits)),"permutations"

i,j,k=0,n-math.factorial(len(digits)-1),math.factorial(len(digits)-1)
print i,j,k

while(j>=0):
	i=i+1
	j=j-k

print "first digit is",digits[i]

del digits[i]

print "numbers remaining:",digits

n=n-(math.factorial(len(digits))*(i+1))
print n

print "digits change in the place every",math.factorial(len(digits)-1),"numbers"
print "there are a total of",math.factorial(len(digits)),"permutations"

i,j,k=0,n-math.factorial(len(digits)-1),math.factorial(len(digits)-1)
print i,j,k

while(j>0):
	i=i+1
	j=j-k

print i
print "second digit is",digits[i]

del digits[i]

print "numbers remaining:",digits

