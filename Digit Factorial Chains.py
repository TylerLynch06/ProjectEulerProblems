import math

def digitFactorial(i):
    sum=0
    num = str(i)
    digits = [int(value) for value in num]
    for digit in digits:
        sum+=math.factorial(digit)
    return sum

def digitFactorialChain(num):
    previousNums=[num]
    i = 0
    while (num not in previousNums) or i==0:
        ##print(num)      
        previousNums.append(num)
        num = digitFactorial(num)    
        i+=1
    return i

chains = 0

for i in range(1,1000000):
    if digitFactorialChain(i) == 60:
        chains+=1
    if i%100000==0: print(f"Of {i} : {chains}/1,000,000")
print(chains)
