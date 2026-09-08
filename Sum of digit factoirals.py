def factorial(i):
    m = 1
    for n in range(i): m*=(n+1)
    return m

def getDigits(num):
    total=0
    num = str(num)
    digits = []
    for digit in num:
        digits.append(int(digit))
    return digits

def digitSum(num):  return sum(getDigits(num))

def digitFactorialSum(num):
    total=0
    for digit in getDigits(num): total+=factorial(digit)
    return total

global results
results = [] 
for i in range(150):
    ##number = int(input("Number: "))
    sumDigits = digitSum(digitFactorialSum(i+1))
    print(f"{i+1}: {sumDigits}")
    for result in results:
        if result[i+1]==sumDigits:
            sumDigits==
    result = [i+1,sumDigits]
    results.append(result)

for result in results: print(result)
