def getRecurrenceLength(num):
    t=1
    while num%2==0:
        num//=2
    while num%5==0:
        num//=5
    if num == 1: return 0
    while (10**t)%(num) != 1:
        t+=1
    return t

greatest = 0
greatestNum = 0
for num in range(1,1000):
    length = getRecurrenceLength(num)
    print(num,length)
    if length>greatest:
        greatest = length
        greatestNum = num
print(greatestNum,greatest)
