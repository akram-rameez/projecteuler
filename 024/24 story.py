# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120  201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# 1  0123
# 2  0132
# 3  0213
# 4  0231
# 5  0312
# 6  0321
# 7  1023
# 8  1032
# 9  1203
# 10 1230
# 11 1302
# 12 1320
# 13 2013
# 14 2031
# 15 2103
# 16 2130
# 17 2301
# 18 2310
# 19 3012
# 20 3021
# 21 3102
# 22 3120
# 23 3201
# 24 3210

import math

digits = [0,1,2,3]
digits.sort()
# print "Number of digits:",len(digits)
# print "digits:",digits

n = 23
n = n-1

# print "digits change in the place every",math.factorial(len(digits)-1),"numbers"
# print "there are a total of",math.factorial(len(digits)),"permutations"

i = int(n/math.factorial(len(digits)-1))
# print i
# print "first digit is",digits[i]

print digits[i],


del digits[i]

# print "numbers remaining:",digits

n=n%(i*math.factorial(len(digits)-1))
# print n

# print "digits change in the place every",math.factorial(len(digits)-1),"numbers"
# print "there are a total of",math.factorial(len(digits)),"permutations"

i = int(n/math.factorial(len(digits)-1))
# print i,n
# print "second digit is",digits[i]

print digits[i],
del digits[i]

# print "numbers remaining:",digits

n=n%(i*math.factorial(len(digits)-1))
# print n

# print "digits change in the place every",math.factorial(len(digits)-1),"numbers"
# print "there are a total of",math.factorial(len(digits)),"permutations"

i = int(n/math.factorial(len(digits)-1))
# print i,n
# print "third digit is",digits[i]

print digits[i],
del digits[i]

# print "numbers remaining:",digits

n=n%(i*math.factorial(len(digits)-1))

# n=n%(i*math.factorial(len(digits)-1))
# print n

# print "digits change in the place every",math.factorial(len(digits)-1),"numbers"
# print "there are a total of",math.factorial(len(digits)),"permutations"

i = int(n/math.factorial(len(digits)-1))
# print i,n
# print "fourth digit is",digits[i]

print digits[i],

del digits[i]

# print "numbers remaining:",digits