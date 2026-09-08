##Problem 23
def getDivisors(n):
    divisors = set()
    divisors.add(1)
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            divisors.add(n//i)
            if (i!=n//i and i not in divisors):
                divisors.add(i)
    return divisors

def divisorSum(n):
    return sum(getDivisors(n))

def canBeSum(n,_list):
    for value in _list:
        if n-value in _list:
            return True
    return False

abundantNums = set()
for i in range(1,28124):
    divSum = divisorSum(i)
    if divSum>i:
        abundantNums.add(i)

print(abundantNums)

validNums = set()
for i in range(24,28200):
    print(i)
    if canBeSum(i,abundantNums):
        validNums.add(i)   
        
print(validNums)
print("Complete")
