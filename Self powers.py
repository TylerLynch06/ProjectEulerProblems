n = 1000
choppedValues = []
for r in range(1,n+1):
    if len(str(r*r))<10:
        choppedValues.append(r**r)
    else: 
        choppedValues.append(int(str(r**r)[-10:]))
print(sum(choppedValues))      
print(str(sum(choppedValues))[-10:])
