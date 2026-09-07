totalSum = 0
for i in range(10,4000000,1):
    if (i%10**(len(str(i))-1)!=0):
        digits = str(i)
        tempSum=0
        for digit in digits:
            tempSum+=int(digit)**5
        if tempSum==i:
            print(i)
            totalSum+=i
print("---Terminated---")
print("\n"+str(totalSum))
