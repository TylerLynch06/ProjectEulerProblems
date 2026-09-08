def Nsum(n):
    return (n/2)*(n+1)

def getPrimeFactors(num):
    tempFactors = []
    run = True
    for i in range(2,int((num//2)+1)):
        if num%i==0 and run==True and i !=num:
            tempFactors.append(i)
            tempFactors.append(num//i)
            for factor in tempFactors:
                if len(getPrimeFactors(factor))==0:
                    if factor not in primeFactors:
                        uniqueFactors[factor] = 1
                    else:
                        uniqueFactors[factor]+=1
                    primeFactors.append(factor)
                    #print(f"{factor} is prime")
                #else: print(f"{factor} is not prime")
            run = False
        if not run: break
    return tempFactors

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

def findDivisors(numDict):
    keys = numDict.keys()
    factorCount = 1
    for key in keys:
        factorCount*=numDict[key]+1
    return factorCount



factorCount=0
i=0
while factorCount<=500:
    i+=1
    primeFactors = []
    uniqueFactors = {}
    getPrimeFactors(Nsum(i))
    factorCount = findDivisors(uniqueFactors)
    if i%1==0: print(f"Index - {i} : Number - {Nsum(i)} : Factor Count - {factorCount}")
print(f"Index - {i} : Number - {Nsum(i)} : Factor Count - {factorCount}")

