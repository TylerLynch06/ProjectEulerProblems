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
        return self.primes[int(num)]

    def countPrimes(self):
        return len([prime for prime in self.primes if prime==True])
        
    def getPrimes(self):
        return [i for i in range(len(self.primes)) if self.primes[i]]

def isTruncatable(x):
    num1 = x
    num2 = x
    for i in range(1,len(str(x))):
        num1 = str(x)[:-i]
        num2 = str(x)[i:]
        if not s.isPrime(int(num1)) or not s.isPrime(int(num2)):
            return False
    return True

    
s = primeSieve(1000000)
primes = s.getPrimes()
primes.sort(reverse=True)
TruncSum = 0
count = 0
specialCases = [2,3,5,7]
for prime in primes:
    if isTruncatable(prime) and prime not in specialCases:
        count+=1
        TruncSum+=prime
print(TruncSum)
print(count)
