def sumSD(x):
    value = 0
    for n in str(x): value+=int(n)**2        
    ##print(value)
    return value

happy=0
iterator = 50
for i in range(iterator):
    #num = int(input("Enter number: "))
    num = i
    print(f"{i}: ",end='')
    previousNumbers = []
    determined = False
    while determined == False:
        num = sumSD(num)
        for number in previousNumbers:
            if number  == num:
                print("SAD")
                determined = True
        previousNumbers.append(num)
        
        if num == 1:
            print("HAPPY")
            happy+=1
            determined = True
print(f"Happy numbers: {happy}\nSad numbers: {iterator-happy}")    



        
        
    
