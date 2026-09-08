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

s = primeSieve(1000000)

for i in range(9,100000):
    valid = False
    if not s.isPrime(i) and i%2==1:
        for n in range(i-1):
            ##print(i)
            if i>(2*(n**2)) and s.isPrime(i-(2*(n**2))):
                valid = True
        if not valid: print(i)
print("Done")
