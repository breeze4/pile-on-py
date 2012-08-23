#card class

class Card: #add __ before a class name to make it private
    
    def __init__(self, val=0, col=None):
        self.value = val #int: 1-10
        self.color = col #char: R,G,B,Y
        self.behavior = None
        self.next = None #another Card

    def __str__(self):
        return self.color + str(self.value)
    
    def getColor(self):
        return self.color

    def getValue(self):
        return self.value

    def getBehavior(self):
        return self.behavior

    def hasNext(self):
        return self.next != None

    def setNext(self, nextCard):
        self.next = nextCard

    
class Deck:
    
    import random
    
    def __init__(self, length=0):
        self.head = None
        self.tail = None
        self.length = length   

    def __str__(self):
        #returns a string representation of the deck
        representation = []
        currCard = self.head
        while currCard.hasNext():
            representation.append(str(currCard))
            currCard = currCard.next
        representation.append(str(currCard))
        return str(representation)        

    def createDeck(self):
        #create 4 cards of each color with the same value
        prevCard = None
        for x in range(1,(self.length/4)+1):
            card1, card2, card3, card4 = Card(x,'R'), Card(x,'G'), Card(x,'B'), Card(x,'Y')
            if x == 1: #if this is the first pass, set the head card
                self.head = card1
            elif x != 1: #if this is not the first or last, add this set of cards to the previous tail
                prevCard.setNext(card1)
            card1.setNext(card2)
            card2.setNext(card3)
            card3.setNext(card4)
            self.tail = card4
            prevCard = card4
    
    def removeCard(self, n):
        #removes and returns the Nth card, starting with the head being card "1"
        cnt = n
        currCard = self.head
        prevCard = None
        if cnt == 1: #if the card to be removed is the head, make a new head
            self.head = currCard.next
        while cnt > 1: #move through the deck until the Nth card is reached
            prevCard = currCard
            currCard = currCard.next
            cnt -= 1
        if prevCard != None: #connect the previous card to the next card in the deck
            prevCard.next = currCard.next
        if n == self.length: #if the card to be removed is the tail, make a new tail
            self.tail = prevCard
        currCard.next = None #delete the connection to the next card from the card to be removed
        self.length -= 1 #decrement the length
        return currCard

    def addCardToEnd(self, cardToAdd):
        #adds the passed card to the end of the deck and updates the tail
        self.tail.next = cardToAdd
        self.tail = cardToAdd
        self.tail.next = None
        self.length += 1

    
    def shuffle(self):
        #shuffles the deck with an adapted Knuth-Fisher-Yates shuffle
        import random
        print "shuffling deck"
        cnt = self.cardCount()
        #remove a random card from the deck and add it to the end until every card has been moved
        while cnt > 0:
            cardNumToShuffle = random.randint(1,cnt)
            self.addCardToEnd(self.removeCard(cardNumToShuffle))
            cnt -= 1
        
    def cardCount(self):
        ##returns the number of cards in the deck
        ##note: while the deck is being shuffled, there is going to be 39 cards in the deck
        ##so this method should not be used if the deck is being shuffled
        ##if it is used during a shuffle, cards get dropped each time a card is removed/added
        if self.head != None:
            cnt = 1
            currCard = self.head
            while currCard.hasNext():
                cnt += 1
                currCard = currCard.next
        else:
            cnt = 0
        return cnt

    

class Hand:

    def __init__(self):
        self.cards = []

    def __str__(self):
        representation = "player hand: "
        for x in self.cards:
            representation += (str(x) + " ")
        return representation.rstrip()

    def addCardToHand(self, cardDealt):
        self.cards.append(cardDealt)
    
    def removeCard(self, cardPlayed):
        self.cards.remove(cardPlayed)
        

class Pile:

    def __init__(self):
        self.topCard = None

    def __str__(self):
        return str(self.topCard)

    def addCardToPile(self, cardPlayed):
        #add card to pile if the value or color matches and compute score increase
        pointsGained = 0
        if self.topCard == None:
            self.topCard = cardPlayed
        #compute the score increase if a value match
        elif (cardPlayed.getValue() == self.topCard.getValue()) and (cardPlayed.getColor() != self.topCard.getColor()):
            pointsGained = self.computeValueScoreIncrease(cardPlayed)
        #compute the score increase if a color match
        elif (cardPlayed.getColor() == self.topCard.getColor()) and (cardPlayed.getValue() != self.topCard.getValue()):
            pointsGained = self.computeColorScoreIncrease(cardPlayed)
        #compute the score increase if a color AND value match (note this won't happen in 40 card games)
        elif (cardPlayed.getColor() == self.topCard.getColor()) and (cardPlayed.getValue() == self.topCard.getValue()):
            pointsGained = self.computeColorValueScoreIncrease(cardPlayed)
        return pointsGained    

    def computeValueScoreIncrease(self, cardPlayed):
        return self.topCard.getValue() + cardPlayed.getValue()

    def computeColorScoreIncrease(self, cardPlayed):
        return 2*(self.topCard.getValue() + cardPlayed.getValue())
        
    def computeColorValueScoreIncrease(self, cardPlayed):
        return 10*(self.topCard.getValue() + cardPlayed.getValue())
