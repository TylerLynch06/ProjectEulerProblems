def fibonacci(max):
    n1=1
    n2=0
    for i in range(max):
        print(n2)
        n2+=n1
        n1=n2-n1
fibonacci(5)
