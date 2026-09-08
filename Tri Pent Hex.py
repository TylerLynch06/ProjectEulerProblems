def hexagonal(x):
    return x*((2*x)-1)

def isTriangleNum(num):
    n = ((2*num)+(0.25))**0.5-(0.5)
    return str(n).split(".")[-1] == "0"

def isPentagonalNum(num):
    n = ((((24*num+1))**0.5)+1)/6
    return str(n).split(".")[-1] == "0"
    
run = True
n = 0
while run:
    n+=1
    num = hexagonal(n)
    if isTriangleNum(num) and isPentagonalNum(num):
        print(num)
