import math

def dot(x,y):
    sum=0
    for i in range(len(x)):
        sum+=x[i]*y[i]
    return sum


def pythag(x):
    return ((x[0]**2)+(x[1]**2))**0.5

def norm(x):
    normX = x
    coeff = pythag(x)
    normX[0], normX[1] = x[0]/coeff, x[1]/coeff
    return normX
    
def incidentRayDir(x1,x2):
    i = [0,0]
    for axis in range(2):
        i[axis] = x2[axis]-x1[axis]
    return i

##N is normalised normal to reflection    
def reflectRayDir(d,n):
    ## r = d -2(d . n)n
    r = [0,0]
    dotProd = dot(d,n)
    print("Incdient Ray: ", d)
    print("Normal: ", n)
    print("Dot: ", dotProd)
    for axis in range(2):
        r[axis] = d[axis]-(dotProd*(n[axis])*2)
    return r

def reflectedRay(x2,dir):
    return (f"y = {x2[1]}+{dir[1]/dir[0]}(x - {x2[0]})")

def normalToEllipse(x2):
    n = [x2[1],4*x2[0]]
    return norm(n)

def solution(y2,m,x2):
    disc = (25*(m**2))-((m**2)*(x2**2))+(2*m*y2*x2)+100-(y2**2)
    numerator = -(y2*m)+((m**2)*x2)-(2*(disc**0.5))
##    disc = ((m**2)*((y2-m)**2)-
##            ((4+(m**2))*(((m**2)*(x2**2))-(2*m*y2+(y2**2)-100))))**0.5
##    numerator = (-m*(y2-m))-disc
    denom = 4+(m**2)
    return numerator/denom

def getY(x,x2,m):
    y = 100-((4)*(x**2))##x2[1]+(m*(x-x2[0]))
    return y

x1 = [0,10.1]
x2 = [1.4, -9.6]
##n= [1,0]

d = norm(incidentRayDir(x1,x2))
n = normalToEllipse(x2)
rd = reflectRayDir(d,n)
m = rd[1]/rd[0]
##print("T: ", norm(x2))
print("Reflected Ray dir: ",rd)
print("\nRefected Ray: ", reflectedRay(x2,rd))
##print("M: ",m)
m=-0.5
x = solution(x2[1],m,x2[0])
y = getY(x,x2,m)
print((x,y))

##print(rd[1]/rd[0])

##def angleBetweenTwoVectors(x,y):
##    dotProd = dot(x,y)
##    modProd = pythag(x)*pythag(y)
##    return math.pi-math.acos(dotProd/modProd)
##
##def reflectedAngle(x2,theta):
##    if x2[1]==0: return math.pi/2
##    angle = (1.5*math.pi)-math.atan2(x2[1],x2[0])-theta
##    return angle
##
##def reflectedGradient(reflectedAngle):
##    return math.tan(reflectedAngle)
##
##
##def solutionNeg(y2,m,x2):
##    disc = (25*(m**2))-((m**2)*(x2**2))+(2*m*y2*x2)+100-(y2**2)
##    numerator = -(y2*m)+((m**2)*x2)+(2*(disc**0.5))
##    denom = 4+(m**2)
##    return numerator/denom
##
##

##
##i=0
##
##x1 = [0,10.1]
##x2 = [1.4,-9.6]
###r1 = [x1[0]-x2[0],x1[1]-x2[1]]
##
##while x2[0]>0.1 or x2[0]<0.1:
##    r1 = [x1[0]-x2[0],x1[1]-x2[1]]
##    theta = angleBetweenTwoVectors(r1,[-4*x2[0],x2[1]])
##    ##print(math.degrees(theta))
##    ##print(math.degrees(reflectedAngle(x2,theta)))
##    ##print("Gradient of reflection: ", reflectedGradient(reflectedAngle(x2,theta)))
##    m = reflectedGradient(reflectedAngle(x2,theta))
##    if i ==1: x = solutionNeg(x2[1],m,x2[0])
##    else: x = x = solution(x2[1],m,x2[0])
##    y = getY(x,x2,m)
##    print(x,y)
##    x1=x2
##    x2=[x,y]
##    i+=1


