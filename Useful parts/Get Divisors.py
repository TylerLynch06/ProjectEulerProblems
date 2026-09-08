def getFactors(num):
    factors=[]
    for i in range(1,int(num//2)):
        if num%i==0 and (i not in factors):
            factors.append(int(i))
            factors.append(int(num//i))
    factors.sort()
    return factors
