singularIntTriangles = 0
solutionCount=0
p=0

while p<=1000:
    a=1
    b=1   
    solutions = 0
    while a<(p+1)//2:
        b=a
        while b<(p+1)//2:
            b+=1
            c=p-(a+b)
            if a+b+c == p and (a**2)+(b**2)==c**2:
                solutions+=1
                #print(f"Solution for Triangle Perimeter {p} : {a,b,c}")
            ##print(a,b,c)                
        a+=1
    if solutions==1:
        singularIntTriangles +=1
    p+=1
print(singularIntTriangles)
