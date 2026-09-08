##Problem 40
Champer = "0."
n=0
while True:
    n+=1
    Champer+=str(n)
    if n==1000: break
fractionalPart = 100
print(Champer[fractionalPart+1])
