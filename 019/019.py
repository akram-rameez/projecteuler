# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def next_month(d,m,y):
	if m==2:
		if y%4==0:
			if y%100!=0 or y%400==0:
				d+=1
			else:
				d+=0
		else:
			d+=0
	else:
		if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
			d+=3
		else:
			d+=2
	if d>6:
		d-=7
	return d
	
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

sum,d=0,0

for x in xrange(1900,2001):
	for y in xrange(1,13):
		if x>1900:
			if d==6:
				sum+=1
		d=next_month(d,y,x)

print sum