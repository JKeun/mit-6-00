###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes
packages = (13, 15, 20)
packages = (1, 3, 7)
packages = (7, 11, 17)

for n in range(1, 150):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
    
    solution = (0, 0, 0)
    x, y, z = packages
    for a in range(0, n//x+1):
        for b in range(0, n//y+1):
            for c in range(0, n//z+1):
                if a*x + b*y + c*z == n:
                    solution = (a, b, c)
    
    if solution == (0, 0, 0):
        bestSoFar = 0
    else:
        bestSoFar += 1

    if bestSoFar == x:
        print("Given pagkage size", packages[0],",", packages[1],"," "and", packages[2], "the largest number of McNuggets that cannot be bought in exact quantity is:", n-a)
