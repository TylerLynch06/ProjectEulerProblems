import turtle
import tkinter
import pygame

vec = pygame.math.Vector2
vector = vec(5,0)
print(vector)

turtle.bgcolor("black")
turtle.color("white")
turtle.speed(0)

def DrawEllipseY(x):
    ##4x^2+y^2=100
    ##+-(100-4x^2)**0.5=y
    y = (100-(4*(x**2)))**0.5
    return (y,-y)

def drawLinePoints(P1,P2):
    turtle.penup()
    turtle.setpos(P1[0]*pointFactor,P1[1]*pointFactor)
    turtle.pendown()
    turtle.setpos(P2[0]*pointFactor,P2[1]*pointFactor)

def drawLineGrad(p1,m,length=10):
    turtle.penup()
    pos=[p1[0]*pointFactor,p1[1]*pointFactor]
    turtle.setpos(pos)
    for i in range(-length,length+1,length*2):
        pos=[(p1[0]+i)*pointFactor,(p1[1]+(m*i))*pointFactor]
        turtle.setpos(pos)
        turtle.pendown()

def plotEllipse():
    positivePoints = []
    negativePoints = []

    intervals = 10
    for interval in range(intervals+1):
        x = (interval/intervals)*5
        y = DrawEllipseY(x)
        positivePoints.append([x*pointFactor,y[0]*pointFactor])
        negativePoints.append([x*pointFactor,y[1]*pointFactor])
    negativePoints = negativePoints[::-1]
    positivePoints.sort()
    pointSets = [negativePoints,positivePoints]
    print(pointSets)
    for points in pointSets:
        turtle.penup()
        for point in points:
            turtle.setpos(point[0],point[1])
            turtle.pendown()
        turtle.penup()
        for point in points:
            turtle.setpos(-point[0],point[1])
            turtle.pendown()

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
    #print("Incdient Ray: ", d)
    #print("Normal: ", n)
    #print("Dot: ", dotProd)
    for axis in range(2):
        r[axis] = d[axis]-(dotProd*(n[axis])*2)
    return r

def reflectedRay(x2,dir):
    return (f"y = {x2[1]}+{dir[1]/dir[0]}(x - {x2[0]})")

def normalToEllipse(x2):
    n = [-x2[1],-4*x2[0]]
    return norm(n)

def solution(y2,m,x2):
    if x2>0:
        disc = (25*(m**2))-((m**2)*(x2**2))+(2*m*y2*x2)+100-(y2**2)
        numerator = -(y2*m)+((m**2)*x2)-(2*(disc**0.5))
    else:
        disc = (25*(m**2))-((m**2)*(x2**2))+(2*m*y2*x2)+100-(y2**2)
        numerator = -(y2*m)+((m**2)*x2)+(2*(disc**0.5))
##    disc = ((m**2)*((y2-m)**2)-
##            ((4+(m**2))*(((m**2)*(x2**2))-(2*m*y2+(y2**2)-100))))**0.5
##    numerator = (-m*(y2-m))-disc
    denom = 4+(m**2)
    return numerator/denom

def getY(x,x2,m):
    y = x2[1]+(m*(x-x2[0]))
    return y


##n= [1,0]

pointFactor = 30

x1 = [0,10.1]
x2 = [1.4, -9.6]

#plotEllipse()
for i in range(1000):
    print("Loop")
##    d = norm(incidentRayDir(x1,x2))
##    n = normalToEllipse(x2)
##    rd = reflectRayDir(d,n)
##    m = rd[1]/rd[0]
    #turtle.color("white")
    #drawLinePoints(x1,x2)
    #turtle.color("yellow")
    #drawLineGrad(x2,-4*x2[0]/x2[1])
    #drawLineGrad(x2,x2[1]/(4*x2[0]))
    n=vec(-4*x2[0],-(x2[1])).normalize()
    #print(x2,x1)
    direction = vec(x2[0]-x1[0],
                    x2[1]-x1[1])
    #drawLineGrad(x2,n.y/n.x))
    r = [0,0]
    r[0] = direction.x - (2*(direction.dot(n))*n.x)
    r[1] = direction.y - (2*(direction.dot(n))*n.y)
    slope = r[1]/r[0]
    #print(slope)

    #print(x1,x2)
    x1 = x2
    #print(x1,x2)
    x2 = [0,0]
    #print((4*(x1[0]) - ((slope**2)*x1[0]) + (2*slope*x1[1]))/(-4-(slope**2)))
    x2[0] = (4*x1[0] - slope*slope*x1[0] + 2*slope*x1[1])/(-4-slope*slope)
    x2[1] = slope*(x2[0]-x1[0])+x1[1]
    #print(x1,x2)
    #x2=[x,y]
    if x2[0]<0.01 and x2[0]>-0.01 and x2[1]>0:
        print(i+1)
        break
