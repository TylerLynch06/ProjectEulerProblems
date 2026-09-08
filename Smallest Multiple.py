def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

factors = [11,12,13,14,15,16,17,18,19,20]

for i in range(1,int(factorial(20)/factorial(10))):
    valid = True
    for factor in factors:
        if i%factor!=0:
            ##print(f"{i} is Invalid")
            valid = False
            break
    if valid==True:
        print(i)
        break


