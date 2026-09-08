def lineOfPascalSequence(n):
    rowSequence = []
    a=1
    b=1
    for i in range(n+1):
        rowSequence.append(a**(n-i))
