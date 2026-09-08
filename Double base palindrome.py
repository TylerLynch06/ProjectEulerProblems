def base2(num):
    return int(str(bin(num)[2:]))

def isPalindromic(num):
    halfOne = str(num)[:len(str(num))//2]
    halfTwo = (str(num)[(len(str(num))+1)//2:])[::-1]
    return halfOne==halfTwo

num = base2(3)
print(num)
print(isPalindromic(num))

doubleBasePalindromes = []

for i in range(1,1000000):
    b10 = i
    b2 = base2(i)
    if isPalindromic(b10) and isPalindromic(b2):
        doubleBasePalindromes.append(i)
print(doubleBasePalindromes)
print(sum(doubleBasePalindromes))
