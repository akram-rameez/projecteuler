spiral_size=1001                #size of the spiral, it is always an odd number.
total=1 
num=1                           #this variable will cycle through the elements of the diagonals: 1, 3, 5 etc.


for i in range(1,int((spiral_size+1)/2)): #used (spiral_size+1)/2 to get the number of iterations of the cycle, which means how many times the spiral rotates around its center
        for j in range(4):
                num=num+(i*2)
                total+=num

print(total)
