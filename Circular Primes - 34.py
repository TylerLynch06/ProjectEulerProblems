##Problem 35

from itertools import permutations

##Total numbers to b=then be filtered
class primeSieve:
    
    def __init__(self,totalNums):
        self.primes = [True for i in range(totalNums+1)]
        ##1 and 0 equivalent not prime
        self.primes[0] = False
        self.primes[1] = False
        for index in range(len(self.primes)):
            if self.primes[index]==True:
                for i in range(2*index,totalNums+1,index):
                    self.primes[i]=False

    def isPrime(self,num):
        return self.primes[num]

    def countPrimes(self):
        return len([prime for prime in self.primes if prime==True])
        
    def getPrimes(self):
        return [i for i in range(len(self.primes)) if self.primes[i]]


##def permutation(x):
##    x = permutations([digit for digit in str(x)], len(str(x)))
##    permList = []
##    for perm in x:
##        permutationBase10 = ""
##        for digit in perm:
##            permutationBase10+=digit
##        permList.append(int(permutationBase10))
##    return permList

def numRotation(x):
    num = str(x)
    rotatedNums = []
    for i in range(len(str(x))):
        num = num[-1]+num[:-1]
        rotatedNums.append(int(num))
    #print(rotatedNums)
    return rotatedNums
        

def isCircular(x):
    valid = True
    primePerms = numRotation(x)
    ##print([perm for perm in primePerms])
    for num in primePerms:
        ##print(f"{num} : {s.isPrime(num)}")
        if not s.isPrime(num):
            valid = False
            break
    return valid

s = primeSieve(1000000)
primes = s.getPrimes()
print(len(primes))
print("Got Primes")

circularPrimeSet = set({})

for prime in primes:
    if isCircular(prime):
        circularPrimeSet.add(prime)
print(circularPrimeSet)
print(len(list(circularPrimeSet)))
print("Done")
    
