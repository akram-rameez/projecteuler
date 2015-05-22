# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

# list of all permutations
# permutations=["0123","0132","0213","0231","0312","0321","1023","1032","1203","1230","1302","1320","2013","2031","2103","2130","2301","2310","3012","3021","3102","3120","3201","3210"]

# list of all digits
digits = ['0','1','2','3','4','5','6','7','8','9']

# just to be sure
digits.sort()

# list to append all digits in
ans=[]
n=999999
# rans=n

# print "actual answer   :",permutations[rans]
# print "=========================================="

# print "Number of digits:",len(digits)
# print "digits:",digits

# print "we need the",n,"th permutation"

# ctr=1

while(not n==0):

	i = int(n/math.factorial(len(digits)-1))
	fact = math.factorial(len(digits)-1)
	rem = n%math.factorial(len(digits)-1)

	# print "-----"
	# print i,"*",math.factorial(len(digits)-1),"+",n%math.factorial(len(digits)-1),"=",n
	# print "i before int:",n*1.0/math.factorial(len(digits)-1)

	# ans=10*ans+digits[i]
	# print ctr,"digit is",digits[i]
	# print "-----"
	ans.append(digits[i])
	del digits[i]

	# ctr=ctr+1
	n=rem

for x in digits:
	ans.append(x)

# ans.append(digits[n2%2])
# del digits[n2%2]
# ans.append(digits[0])

# print "--------------------"
print ''.join(ans)
# print "actual answer   :",permutations[rans]