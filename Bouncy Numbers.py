def isBouncy(num):
    increasing = False
    decreasing = False
    num = str(num)
    lastDigit = num[0]
    for digit in num[1:]:     
        if lastDigit>digit:
            decreasing=True
        if lastDigit<digit:
            increasing=True
        lastDigit = digit
        if increasing and decreasing:
            return True
    return False

i=0
bouncyCount = 0
proportion = 0

while proportion<99:
    i+=1
    if isBouncy(i): bouncyCount+=1
    if bouncyCount==0: proportion=0
    else: proportion = (bouncyCount/i)*100
print(i)
print(proportion)
print(bouncyCount)
