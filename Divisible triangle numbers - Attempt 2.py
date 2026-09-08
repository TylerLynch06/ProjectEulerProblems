def getFactors(num):
    factors=[]
    for i in range(1,int(num//2)):
        if num%i==0 and (i not in factors):
            factors.append(int(i))
            factors.append(int(num//i))
    factors.sort()
    return factors

def Nsum(n):
    return (n/2)*(n+1)

factorCount=0
i = 0
while i<3:
    i+=1
    currentNum = Nsum(i)
    factors = getFactors(currentNum)
    factorCount = len(factors)
    print(factors)
    if i%10==0: print(i,currentNum)
print(f"Triangle Number - {int(currentNum)} : Factors - {factorCount}")
