from fractions import Fraction
from decimal import Decimal

def convergence(x=1,n=0,conMax=0):
    if n>=conMax: return 0
    x = Fraction(1,2+convergence(1,n+1,conMax))
    return x

##Counts how many times numerator is LONGER than denominator
lopsideCount = 0
convergents = []   
for i in range(1,1001):
    approx = 1 + convergence(1,conMax=i)
    ##print(approx)
    convergents.append(approx)
    if len(str(approx.numerator))>len(str(approx.denominator)): lopsideCount+=1
print(approx.numerator/approx.denominator)
print(convergents)
print(lopsideCount)
print("OVER")
