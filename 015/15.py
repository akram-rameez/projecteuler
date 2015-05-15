# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

n = 21

# Creates a list containing n lists initialized to 0
a = [[0 for x in range(n)] for x in range(n)]

for x in xrange(0,n):
	a[x][0] = 1

for x in xrange(1,n):
	a[0][x] = 1

for x in xrange(1,n):
	for y in xrange(1,n):
		a[x][y] = a[x-1][y]+a[x][y-1]

print a[n-1][n-1]