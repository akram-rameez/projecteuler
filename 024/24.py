# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

permutations=["0123","0132","0213","0231","0312","0321","1023","1032","1203","1230","1302","1320","2013","2031","2103","2130","2301","2310","3012","3021","3102","3120","3201","3210"]
digits = ['0','1','2','3']
digits.sort()
ans=[]
n=23
rans=n
print "Number of digits:",len(digits)
print "digits:",digits

print "we need the",n+1,"permutation"

ctr=1

while(len(digits)>0):

	print "--------------------"

	print "digits change in the place every",math.factorial(len(digits)-1),"numbers"
	print "there are a total of",math.factorial(len(digits)),"permutations"

	i = int(n/math.factorial(len(digits)-1))
	print "i before int:",n*1.0/math.factorial(len(digits)-1)

	# ans=10*ans+digits[i]
	print ctr,"digit is",digits[i]
	ans.append(digits[i])
	del digits[i]
	print digits,"-----"
	if i==0:
		for x in digits:
			ans.append(x)
			# ans=10*ans+digits[i]
		break

	n=n%(i*math.factorial(len(digits)-1))

print "--------------------"
print "answer obtained :",''.join(ans)
print "actual answer   :",permutations[rans]