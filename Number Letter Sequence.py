numberCharacters = {0 : 4,
                    1 : 3,
                    2 : 2,
                    3 : 5,
                    4 : 4,
                    5 : 4,
                    6 : 3,
                    7 : 5,
                    8 : 5,
                    9 : 4,
                    10 : 3,
                    11 : 6,
                    12 : 6,
                    13 : 8,
                    14 : 8,
                    15 : 7,
                    16 : 7,
                    17 : 9,
                    18 : 9,
                    19 : 8,
                    20 : 6,
                    30 : 6,
                    40 : 5,
                    50 : 5,
                    60 : 5,
                    70 : 7,
                    80 : 6,
                    90 : 6}

sum = 0
for num in range(1,1000):
    print("loop")
    if int(num[-2]) == 1:
        sum+= numberCharacters[int(str(num[-2])+str(num[-1]))]
    else:
        sum+= numberCharacters[int(num[-2])]+numberCharacters[int(num[-1])]
    if num>100 and (int(num[-1])+int(num[-2])>0):
        sum+=3
    if num>100:
        sum+=7+numberCharacters[num[0]]
sum+=(len("OneThousand"))
    
print(sum)
