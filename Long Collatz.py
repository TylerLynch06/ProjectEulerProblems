def collatz(n, iteration=0):
    ##print(n)
    iteration+=1
    if n==1:return iteration
    elif n%2==0:
        n/=2
    elif n%2==1:
        n=(3*n)+1
    return collatz(n,iteration)
collatzList = [[0,0]]
largestIteration=0
largestIndex=0
for i in range(1,1000000): 
    collatzEntry=[i,collatz(i)]
    collatzList.append(collatzEntry)
    print(f"Index: {i}, Iterations: {collatzList[i][1]}")
    if collatzList[i][1]>largestIteration:
        largestIteration=collatzList[i][1]
        largestIndex=[i][0]
print(largestIndex)
input("End: ")
