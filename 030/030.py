numdigits=[]
numvalue=2
solutions=[]

while numvalue>=2 and numvalue<355000:  #5*9^5 is a 6 digit number, 6*9^5 is still a 6 digit number, so it is the max value we can iterate on
    numvalue+=1
    numdigits=list(str(numvalue))
    x=0
    for digit in range(len(numdigits)):
        x+=((int(numdigits[digit]))**5)
    if x==numvalue:
        solutions.append(x)
print(sum(solutions))

