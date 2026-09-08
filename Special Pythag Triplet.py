def con1(a,b,c):
    return a+b+c==1000

def con2(a,b,c):
    return (a**2)+(b**2)==c**2


run = True
a=0
b=0
c=0

for i in range(500):
    a+=1
    ##print(a)
    for n in range(a,500):
        b=n
        c=1000-(a+b)
        ##print(con1(a,b,c))
        if con1(a,b,c) and con2(a,b,c):
            print(a,b,c)
            print(a*b*c)

input()
