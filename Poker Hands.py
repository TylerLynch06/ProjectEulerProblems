def IsRoyalFlush(cardSet):
    royalFlush = IsFlush(cardSet)[0] and IsStraight(cardSet)[0] and IsHighCard(cardSet)[2]=="A"
    if (not royalFlush): return [False]
    else: return [True, f"Royal Flush : {IsFlush(cardSet)[1]} and {IsStraight(cardSet)[1]}"]

def IsStraightFlush(cardSet):
    straightFlush = IsFlush(cardSet)[0] and IsStraight(cardSet)[0]
    if (not straightFlush): return [False]
    else:
        return [True, f"Straight Flush : {IsFlush(cardSet)[1]} and {IsStraight(cardSet)[1]}",highestCard]

def IsFourOfAKind(cardSet):
    cards = cardOccurrence(cardSet)
    for n in cards:
        if cards[n]==4:
            return [True, f"Four of a kind of {n}(s)",n]
    return [False]

def IsFullHouse(cardSet):
    occurrence = cardOccurrence(cardSet)
    if len(occurrence)>2: return [False]
    threePair = None
    twoPair = None

    for cardValue in occurrence:
        if occurrence[cardValue] == 3 and threePair==None:
            threePair = cardValue
        if occurrence[cardValue] == 2 and twoPair==None:
            twoPair = cardValue
    if (threePair != None and twoPair!=None):
        return [True, f"Full House with Two Pair {twoPair} and three pair {threePair}",(threePair,twoPair)]
    else: return [False]

def IsFlush(cardSet):
    initialSuit = cardSet[0].att["suit"]
    for card in cardSet:
        if card.att["suit"]!=initialSuit: return [False]
    return [True, f"Flush of suit {initialSuit}"]

def IsStraight(cardSet):
    highestCard = IsHighCard(cardSet)[2]
    index = cardValue.index(highestCard)
    if (highestCard=="A"):
        if (SpecialWheelStraight(cardSet)[0]):
            ##raise Exception("Wheel Straight Found")
            return [True, f"Straight from A to 5",highestCard]
    if (index+5>13):
        return [False]
    validValues = [cardValue[i] for i in range(index,index+5)]
    for card in cardSet:   
        if card.att["value"] not in validValues:
            return [False]
        else: validValues.remove(card.att["value"])
    return [True, f"Straight from {cardValue[index+4]} to {highestCard}",highestCard]

def SpecialWheelStraight(cardSet):
    ##raise Exception("wheel straight called")
    validValues = ['A','2','3','4','5']
    for card in cardSet:   
        if card.att["value"] not in validValues:
            print(card.att["value"])
            ##raise Exception("Wheel straight rejected")
            return [False]
        else: validValues.remove(card.att["value"])
    return [True, f"Straight from A to 5","A"]


def IsThreeOfAKind(cardSet):
    cards = cardOccurrence(cardSet)
    for n in cards:
        if cards[n]==3:
            return [True, f"Three of a kind of {n}(s)"]
    return [False]


def IsTwoPairs(cardSet):
    pairCount=0
    parsedPairs = []
    cards = cardOccurrence(cardSet)
    for n in cards:
        if cards[n]>=2 and n not in parsedPairs:
            parsedPairs.append(n)
            pairCount+=1
        if pairCount == 2:
            parsedPairs.sort()
            return [True, f"Pair of {parsedPairs[0]}(s) and {parsedPairs[1]}(s)",parsedPairs]
    return [False]

def IsOnePair(cardSet):
    cards = cardOccurrence(cardSet)
    for n in cards:
        if cards[n]>=2:
            return [True, f"Pair of {n}(s)", [n]]
    return [False]

def IsHighCard(cardSet):
    smallestValue = 20
    highestCardFace = None
    for card in cardSet:
        if smallestValue>cardValue.index(card.att["value"]):
            smallestValue=cardValue.index(card.att["value"])
            highestCardFace=card.att["value"]
    return [True, f"Highest Card of {highestCardFace}",highestCardFace]

def cardOccurrence(cardSet):
    occurrenceDict = {}
    for card in cardSet:
        n = 0
        currentValue = card.att["value"]
        for tempCard in cardSet:
            if tempCard.att["value"]==currentValue:
                n+=1
        occurrenceDict.update({currentValue:n})
    return occurrenceDict

def DrawRoyalFlush(handResult1,handResult2,hand1,hand2):
    print("\n\n\n\n\n\n\n\n\\nn\n\n\n\n\n\n\n\n\n")
    pass

def DrawStraightFlush(handResult1,handResult2,hand1,hand2):
    if cardValue.index(handResult1[-1])<cardValue.index(handResult2[-1]):
        return True
    elif cardValue.index(handResult1[-1])>cardValue.index(handResult2[-1]):
        return False
    return IsP1WinsHighDraw(hand1,hand2)

def DrawFourOfAKind(handResult1,handResult2,hand1,hand2):
    if cardValue.index(handResult1[-1][0])<cardValue.index(handResult2[-1][0]):
        return True
    elif cardValue.index(handResult1[-1][0])>cardValue.index(handResult2[-1][0]):
        return False
    hand1=removeCardFromHand(hand1,handResult1[-1][0])
    hand2=removeCardFromHand(hand2,handResult2[-1][0])

def DrawFullHouse(handResult1,handResult2,hand1,hand2):
    if cardValue.index(handResult1[-1][0])<cardValue.index(handResult2[-1][0]):
        return True
    elif cardValue.index(handResult1[-1][0])>cardValue.index(handResult2[-1][0]):
        return False
    if cardValue.index(handResult1[-1][1])<cardValue.index(handResult2[-1][1]):
        return True
    elif cardValue.index(handResult1[-1][1])>cardValue.index(handResult2[-1][1]):
        return False
    return IsP1WinsHighDraw(hand1,hand2)

def DrawFlush(handResult1,handResult2,hand1,hand2):
    return IsP1WinsHighDraw(hand1,hand2)
    
def DrawStraight(handResult1,handResult2,hand1,hand2):
    if cardValue.index(handResult1[-1])<cardValue.index(handResult2[-1]):
        return True
    elif cardValue.index(handResult1[-1])>cardValue.index(handResult2[-1]):
        return False
    return IsP1WinsHighDraw(hand1,hand2)
    

def DrawThreeOfAKind(handResult1,handResult2,hand1,hand2):
    if handResult1[-1]>handResult2[-1]:
        return True
    elif handResult1[-1]<handResult2[-1]:
        return False
    removeAllCardsOfValueFromHand(hand1,handResult1[-1])
    removeAllCardsOfValueFromHand(hand2,handResult2[-1])
    return IsP1WinsHighDraw(hand1,hand2)

def DrawTwoPairs(handResult1,handResult2,hand1,hand2):
    if cardValue.index(handResult1[-1][0])<cardValue.index(handResult2[-1][0]):
        return True
    elif cardValue.index(handResult1[-1][0])>cardValue.index(handResult2[-1][0]):
        return False
    if cardValue.index(handResult1[-1][1])<cardValue.index(handResult2[-1][1]):
        return True
    elif cardValue.index(handResult1[-1][1])>cardValue.index(handResult2[-1][1]):
        return False
    return IsP1WinsHighDraw(hand1,hand2)

def DrawOnePair(handResult1,handResult2,hand1,hand2):
    if handResult1[-1]>handResult2[-1]:
        return True
    elif handResult1[-1]<handResult2[-1]:
        return False
    hand1=removeCardFromHand(hand1,handResult1[-1])
    hand2=removeCardFromHand(hand2,handResult2[-1])
        
    return IsP1WinsHighDraw(hand1,hand2)
    
def DrawHighCard(handResult1,handResult2,hand1,hand2):
    return IsP1WinsHighDraw(hand1,hand2)


def removeCardFromHand(hand,cardValue):
    for currentCard in hand:
        if currentCard.att["value"] == cardValue:
            hand.remove(currentCard)
            break
    return hand

def removeAllCardsOfValueFromHand(hand,cardValue):
    for currentCard in hand:
        if currentCard.att["value"] == cardValue:
            hand.remove(currentCard)
    return hand

##13
cardValue = ['A','K','Q','J','T','9','8','7','6','5','4','3','2','A']

handList = [IsRoyalFlush,IsStraightFlush,IsFourOfAKind,IsFullHouse,IsFlush,
                IsStraight,IsThreeOfAKind,IsTwoPairs,IsOnePair,IsHighCard]

drawList = [DrawRoyalFlush,DrawStraightFlush,DrawFourOfAKind,DrawFullHouse,DrawFlush,
                DrawStraight,DrawThreeOfAKind,DrawTwoPairs,DrawOnePair,DrawHighCard]

def GetHighestScore(cardSet):
    handIndex = 0
    greatestHand = None
    foundHand = False
    while (not foundHand):
        if (functionList[handIndex](cardSet)==False):
            handIndex+=1         
        else: return functionList[handIndex](cardSet)

def readHand():
##    with open('yourfile.txt', 'r') as file:
##    content = file.read()
##    lines = content.splitlines()
##    for line in lines:
##        print(line)
        
    allHands = []
    file = open("Data\\poker.txt","r")
    print("File Found")
    i=1
    for line in file:
        ##print(line)
        lineText = line
        if lineText[-1] == "\n":
            lineText = line[:-1]
        allHands.append(lineText)
        i+=1
    print("Read Data")
    return allHands

def splitCardsToHand(allCards):
    cardSets = allCards.split(" ")
    P1CardSet = cardSets[0:5]
    P2CardSet = cardSets[5:10]

    p1Hand = ""
    for card in P1CardSet:
        p1Hand+=f"{card} "
    p1Hand = p1Hand[:-1]
    p2Hand = ""
    for card in P2CardSet:
        p2Hand+=f"{card} "
    p2Hand = p2Hand[:-1]
    return p1Hand,p2Hand

def IsP1WinsHighDraw(hand1,hand2):
    ##print(hand1[0].att["value"])
    tempHand1 = hand1
    tempHand2 = hand2
    p1HighCard = None
    p2HighCard = None
    attempts = 0
    while p1HighCard==p2HighCard and attempts<30:
        ##print([card.att["value"] for card in tempHand1],[card.att["value"] for card in tempHand2])
              
        p1HighCard = cardValue.index(IsHighCard(tempHand1)[2])

        p2HighCard = cardValue.index(IsHighCard(tempHand2)[2])

        for card in tempHand1:
            if card.att["value"] == cardValue[p1HighCard]:
                tempHand1.remove(card)
                break

        for card in tempHand2:
            if card.att["value"] == cardValue[p2HighCard]:
                tempHand2.remove(card)
                break
        
        attempts+=1
    return p1HighCard<p2HighCard

class PokerRound:

    def __init__(self, allCards,roundId):

        self.roundId = roundId
        p1Hand, p2Hand = splitCardsToHand(allCards)
                
        
        self.p1Cards = self.giveCards(p1Hand)
        self.p2Cards = self.giveCards(p2Hand)
        self.winningHand = None
        self.handIndex = 0

    def giveCards(self,hand):
        handItems = hand.split(" ")
        cards = []
        for card in handItems:
            cards.append(Card(card[0:-1],card[-1]))
        return cards            

    def play(self):
        player1Wins = False
        ##print(f"{cardOccurrence(self.p1Cards)}\n")
        for hand in handList:            
            P1HandResult = hand(self.p1Cards)
            P2HandResult = hand(self.p2Cards)
            if (P1HandResult[0] and P2HandResult[0]):
                if (drawList[self.handIndex](P1HandResult,P2HandResult,self.p1Cards,self.p2Cards)):
                    player1Wins = True
                    self.winningHand = P1HandResult[1]
                else:
                    player1Wins = False
                    self.winningHand = P2HandResult[1]
                break
            if (P1HandResult[0] and not P2HandResult[0]):
                player1Wins = True
                self.winningHand = P1HandResult[1]
                break
            elif (not P1HandResult[0] and P2HandResult[0]):
                player1Wins = False
                self.winningHand = P2HandResult[1]
                break
            self.handIndex+=1
        return [player1Wins,self.winningHand]
        

class Card:

    def __init__(self,value,suit):
        self.att = {"value":value,"suit":suit}

print(PokerRound("AH 2C 3D 4S 5S 4C 2D 7S 9S 9D",0).play())

allHands = readHand()
allRounds = []

i = 0
for pokerHand in allHands:
    round = PokerRound(pokerHand,i)
    allRounds.append(round)
    i+=1

player1Wins = 0

for round in allRounds:
    roundResult = round.play()
    if roundResult[0]:
        print(f"Player 1 loses : Player 2 wins with {roundResult[1]} : Player 1 has {player1Wins} victories")
    else:
        player1Wins+=1
        print(f"Player 1 wins  : Player 1 wins with {roundResult[1]} : Player 1 has {player1Wins} victories")
print(f"\n{player1Wins}")
