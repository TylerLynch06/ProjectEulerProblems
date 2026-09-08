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

limit = 1000000

sieve = primeSieve(limit)
primes = sieve.getPrimes()

primeLen = len(primes)
longestLen = 0

for i in range(0,1000):
    i = (1000)-i
    for n in range(primeLen-(i)):
        primeSum = sum(primes[n:i+n])
        if primeSum<limit and sieve.isPrime(primeSum):
          longestLen = (i,primeSum)
        if longestLen!=0:
            break
    if longestLen!=0: break
    print(i)
print(longestLen)
