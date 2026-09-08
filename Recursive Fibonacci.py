def fibonacci(max,n1=1,n2=0):
    n1+=n2   
    if max<=1: return n1
    return fibonacci(max-1,n2,n1)
print(fibonacci(max=10))
