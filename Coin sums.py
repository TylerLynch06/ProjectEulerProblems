##Assume 4 orientations to make 5p (inclduing one 5p)

partitionValues = {5 : 4, 10 : 11 , 20 : 41}

def coinPartition(p):
    partition = leastCoinSum(p)
    for coin in partition:
        print(leastCoinSum(coin))


##Least amount of coins to attain the same sum, cannot be equal to original coin
def leastCoinSum(p):
    sum = 0
    chosenCoins = []
    while p!=sum:
        for coin in coins:
            if sum+coin<=p and coin!=p:
                sum+=coin
                chosenCoins.append(coin)
                break
    return chosenCoins
    
##All in pence
coins = [200,100,50,20,10,5,2,1]
    
coinPartition(5)
print("Done")
