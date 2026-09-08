def reversible(num): 
    num = str(num)
    if num[0] =="0" or num[-1] == "0": return False
    reverseNum = num[::-1]
    reverseSum = str((int(num)+int(reverseNum)))
    reverseSum = str(int(reverseSum))
    ##print(f"{int(num)} + {int(reverseNum)} = {reverseSum}")
    for digit in reverseSum:
        if float(digit)%2==0: return False
    reversibles.append(num)
    return True

reversibles = []
count = 0
for i in range(1,1000000000):
    count+=reversible(i)
    if i % 1000000==0: print(i)
print(count)
print(reversibles)
print(len(reversibles))
