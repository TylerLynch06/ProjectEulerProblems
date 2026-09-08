def isPalindromic(num):
    halfOne = str(num)[:len(str(num))//2]
    halfTwo = (str(num)[(len(str(num))+1)//2:])[::-1]
    return halfOne==halfTwo

palindromes = []

for x in range(1,1000):
    for y in range(1,1000):
        prod = x*y
        if isPalindromic(prod):
            palindromes.append(prod)
palindromes.sort()
print(palindromes[-1])
print(palindromes[0])
