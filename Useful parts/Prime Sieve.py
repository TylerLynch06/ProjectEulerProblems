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

s = primeSieve(100000000)

primeCache = open("primeCache.txt","w")
for prime in s.getPrimes():
    primeCache.write(str(prime)+"\n")
primeCache.close()
print("Cached")
