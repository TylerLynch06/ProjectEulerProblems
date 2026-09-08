import math

digitFactorials = []

for i in range(3,10000000):
    sum=0
    num = str(i)
    digits = [int(value) for value in num]
    for digit in digits:
        sum+=math.factorial(digit)
    if sum == i: digitFactorials.append(i)
print(digitFactorials)
