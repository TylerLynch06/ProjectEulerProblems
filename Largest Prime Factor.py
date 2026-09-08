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

for y in range(10):
    for x in range(1,11):
        print((y*10)+x, end=", ")
    

##primeFactors = []
##uniqueFactors = {}
##getPrimeFactors(600851475143)
##print(primeFactors)
##print(uniqueFactors)
