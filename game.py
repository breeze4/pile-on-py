#game class for this card game

import card

class GameMain:
    
    #import card

    def __init__(self):
        self.playerHand = None
        self.gameDeck = None
        self.pile1, self.pile2, self.pile3 = None, None, None
        self.playerScore = 0
        
        
    def initializeGame(self):
        print "welcome to a shitty card game"
        self.gameDeck = card.Deck(40)
        self.gameDeck.createDeck()
        self.gameDeck.shuffle()
        self.playerHand = card.Hand()
        self.pile1 = card.Pile()
        self.pile2 = card.Pile()
        self.pile3 = card.Pile()
        self.startGame()
        self.displayCurrentStatus()
        
    def playGame(self):
        while self.playerScore < 50:
            self.takeInput()
            self.displayCurrentStatus()

    def playToPile(self, destPile, cardPlayed):
        self.updateScore(destPile.addCardToPile(cardPlayed))
        self.playerHand.removeCard(cardPlayed)
        self.dealCardsToPlayer(1)

    def updateScore(self, pointsGained):
        self.playerScore += pointsGained

    def startGame(self):
        self.dealCardsToPlayer(5)
        self.dealCardsToPiles()

    def displayCurrentStatus(self):
        self.displayHand()
        self.displayPiles()
        self.displayScore()
        self.gameDeck.cardCount()

    def displayScore(self):
        print "score: ", self.playerScore

    def displayPiles(self):
        print "pile1:", self.pile1, " pile2:", self.pile2, " pile3:", self.pile3

    def displayHand(self):
        print self.playerHand

    def dealCardsToPlayer(self, numOfCards):
        #deal cards to the player's hand
        for cardIndex in range(0,numOfCards):
            #deal the top card
            cardToDeal = self.gameDeck.removeCard(1)
            self.playerHand.addCardToHand(cardToDeal)

    def dealCardsToPiles(self):
        #deal cards to the piles
        self.pile1.addCardToPile(self.gameDeck.removeCard(1))
        self.pile2.addCardToPile(self.gameDeck.removeCard(1))
        self.pile3.addCardToPile(self.gameDeck.removeCard(1))

    def takeInput(self):
        rawcommand = raw_input("What would you like to do? Enter a command: ")
        command = rawcommand.split()
        print command
        if command[0]=="H1":
            if command[1]=="to":
                if command[2]=="P1":
                    self.playToPile(self.pile1, self.playerHand.cards[0])
                    print "played H1 to P1"
                elif command[2]=="P2":
                    self.playToPile(self.pile2, self.playerHand.cards[0])
                    print "played H1 to P2"
                elif command[2]=="P3":
                    self.playToPile(self.pile3, self.playerHand.cards[0])
                    print "played H1 to P3"
        elif command[0]=="H2":
            if command[1]=="to":
                if command[2]=="P1":
                    self.playToPile(self.pile1, self.playerHand.cards[1])
                    print "played H2 to P1"
                elif command[2]=="P2":
                    self.playToPile(self.pile2, self.playerHand.cards[1])
                    print "played H2 to P2"
                elif command[2]=="P3":
                    self.playToPile(self.pile3, self.playerHand.cards[1])
                    print "played H2 to P3"
        elif command[0]=="H3":
            if command[1]=="to":
                if command[2]=="P1":
                    self.playToPile(self.pile1, self.playerHand.cards[2])
                    print "played H3 to P1"
                elif command[2]=="P2":
                    self.playToPile(self.pile2, self.playerHand.cards[2])
                    print "played H3 to P2"
                elif command[2]=="P3":
                    self.playToPile(self.pile3, self.playerHand.cards[2])
                    print "played H3 to P3"
        elif command[0]=="H4":
            if command[1]=="to":
                if command[2]=="P1":
                    self.playToPile(self.pile1, self.playerHand.cards[3])
                    print "played H4 to P1"
                elif command[2]=="P2":
                    self.playToPile(self.pile2, self.playerHand.cards[3])
                    print "played H4 to P2"
                elif command[2]=="P3":
                    self.playToPile(self.pile3, self.playerHand.cards[3])
                    print "played H4 to P3"
        elif command[0]=="H5":
            if command[1]=="to":
                if command[2]=="P1":
                    self.playToPile(self.pile1, self.playerHand.cards[4])
                    print "played H5 to P1"
                elif command[2]=="P2":
                    self.playToPile(self.pile2, self.playerHand.cards[4])
                    print "played H5 to P2"
                elif command[2]=="P3":
                    self.playToPile(self.pile3, self.playerHand.cards[4])
                    print "played H5 to P3"


game = GameMain()
game.initializeGame()
game.playGame()
