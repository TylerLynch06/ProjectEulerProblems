def pythag(a,b):
    return ((a**2)+(b**2))**0.5

def perimeter(a,b):
    return a+b+(pythag(a,b))

def subArea(a,b,p):
    return p-(a+b)

p=0


solutions = []


while p<=1000:
    halt=False
    solutionCount=0
    a=1
    b=1
    p+=1
    print(p)
    while not halt:
        b+=1
        if pythag(a,b)==subArea(a,b,p):
            solutionCount+=1
        if perimeter(a,b)>=p:
            a+=1
            b=a
            if perimeter(a,b)>=p:
                solutions.append(solutionCount)
                halt=True
print("Done")
indexOfGC = 0
greatestCount = 0
for i,count in enumerate(solutions):
    if count>greatestCount:
        greatestCount=count
        indexofGC=i
    print(f"Perimeter: {i+1} | Solutions: {count}\n")
print(greatestCount)
input()
