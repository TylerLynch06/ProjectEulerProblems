from fractions import Fraction
from decimal import Decimal

def f(seq,max=99,n=0,k=1):
    term = seq[n%len(seq)]
    if term[1]=='K':
        term = term[0]*k
        k+=1
    else: term = term[0]
    if n>=max: return 0
    return Fraction(1,(term+f(seq,max,n+1,k)))

initialTerm = 2
seq = [[1,'L'],[2,'K'],[1,'L'],[1,'L'],[2,'K'],[1,'L'],[1,'L'],[2,'K'],[1,'L']]

approx=initialTerm+f(seq)
print(approx)
sum = 0
for char in str(approx.numerator):
    sum+=int(char)
    print(char,end=" ")
print(f"\nFrac: {approx}")
print(f"\nNumerator: {approx.numerator}")
print(f"\nReal: {approx.numerator/approx.denominator}")
print("END")
print(sum)
