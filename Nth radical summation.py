import numpy as np

## i = 2, hence find the sum of the sum of all r^(2) 
i = 2

coeffMatrix = []
sumMatrix = []
for x in range(1,i+1):
    coeffLine = []
    sumX = 0
    for coeff in range(i,0,-1):
        print(coeff)
        coeffLine.append(x**coeff)
    for r in range(1,x):
        sumX+=r**(i)
    sumMatrix.append(sumX)
    coeffMatrix.append(coeffLine)
    
print(coeffMatrix)
print(sumMatrix)
coeffInverse = np.linalg.inv(coeffMatrix)
unknowns = np.matmul(sumMatrix, coeffInverse)
print(unknowns)
