##EULER 125

import numpy as np

def squareSum(n):
    return n*(n+1)*((2*n)+1)/6

def findN(S,k):
    a=2
    b=3
    c=1
    d=(-(2*(k**3))+(3*k*k)-k-(6*S))
    coeffs = [a,b,c,d]
    p = np.roots(coeffs)
    validRoot = 0
    for root in p:
        print(root)
        if np.isreal(root):
           return [True,np.real(root)]


palindromes = open("Palindrome Cache.txt","r")
values = palindromes.read()
values = values.split("\n")
values = list(map(int,values))
print(len(values),"Palindromes Loaded")

input()

validPalindromes = []
for k in range((10**1)-2,1,-1):
    for palindrome in values:
        palindromeData = findN(palindrome, k)
        if palindromeData[0]:
            palindromeData.insert(1,k)
    print(k)

for n in validPalindromes:
    print(n)
print("\nProgram Complete")
