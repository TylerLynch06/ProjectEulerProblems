def getPrimeFactors(num):
    tempFactors = []
    run = True
    for i in range(2,int((num+1)//2)):
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

##Contain a lsit of N length with all factors
def distinctFactors(factors,k):
    factorCount = 0
    factorsConcat = []
    for factorSet in factors:
        ##print(factors)
        factorCount+=len(factorSet)
        factorsConcat+=factorSet
        if len(factorSet)!=k: return False
    distinctFactors = list(dict.fromkeys(factorsConcat))
    return factorCount==len(distinctFactors)

def normaliseUniqueFactors(uniqueFactors):
    factors = []
    for factor in uniqueFactors.items():
        factors.append(factor[0]**factor[1])
    #print(factors, primeFactors, i, i+1)
    return factors

n = 5
##K = number of factors in each number to be true
k = n
tempFactors = []


for num in range(n):
    primeFactors = []
    uniqueFactors = {}      
    getPrimeFactors(num)
    uniqueFactors = normaliseUniqueFactors(uniqueFactors)
    tempFactors.append(uniqueFactors)

for i in range(n,1000000):
    primeFactors = []
    uniqueFactors = {}      
    getPrimeFactors(i)
    uniqueFactors = normaliseUniqueFactors(uniqueFactors)
    tempFactors.append(uniqueFactors)
    tempFactors = tempFactors[1:]
    ##print(tempFactors)
    distinct = distinctFactors(tempFactors,k)
    #print()
    if i%5000 == 0: print(i)
    if distinct:
        print([num for num in range(i-n+1,i+1)])
        break

    
