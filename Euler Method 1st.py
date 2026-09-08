def quadraticDifferential(x):
    return ((x**2)*3)+(x*2)

def EulerMethod(y, x, derivative, step, toMax, iterations=0):
    gradient = float(derivative(x))
    print(f"({round(x,3)},{round(y,3)}) | Gradient: {round(gradient,3)}")
    if iterations>=toMax: return gradient*step+y
    return EulerMethod(gradient*step+y, x+step,derivative, step, toMax, iterations+1)

##def sigFig(figure, sigFigs):
##    result=str(figure)
##    if len(result)<sigFigs:
##        result+="."
##        for i in range(sigFigs-len(result)): result+="0"
##    if len(result)>sigFigs:
##        roundDigit = str(round(float(f"{result[sigFigs-1]}.{result[sigFigs]}{result[sigFigs+1]}")))
##        result = result[:sigFigs-1]+roundDigit+result[sigFigs:]
##        sigValues = result[:sigFigs]
##        for i in range(len(result)-sigFigs): sigValues+="0"
##        result=sigValues
##    return result

##print(sigFig(12565,5))

h = float(input("Input Step Value: "))
x = float(input("Enter X0: "))
y = float(input("Enter Y0: "))

EulerMethod(y,x,quadraticDifferential,h,5)
