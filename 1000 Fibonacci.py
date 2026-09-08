def fibonacci(digits,a=1,b=1):
    index=2
    digit = 0
    while digits>digit:     
        a=a+b
        index+=1
        tempA = a
        a=b
        b=tempA
        digit = len(str(b))
        #print(b,index,digit)
    return(b,index)

fib = fibonacci(1000)
print(f"\nValue: {fib[0]}\nIndex: {fib[1]}")
