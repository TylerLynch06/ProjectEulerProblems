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

def isPandigital(num):
    n = len(str(num))
    digits = [i for i in range(1,n+1)]
    ##print(digits)
    num = str(num)
    for char in num:
        if int(char)>n:
            return False
        elif int(char) in digits:
            digits.remove(int(char))
        elif char not in digits:
            return False
    return True
    

sieve = primeSieve(1000000000)
print("Primes Filtered")
primes = sieve.getPrimes()
print("Primes Retrieved")
panPrimes = []

for prime in primes:
    if isPandigital(prime):
        panPrimes.append(prime)

panPrimes.sort()
print(panPrimes)
print(panPrimes[-1])
print(panPrimes[1])
print("Done")

