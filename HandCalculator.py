class Play:
    def __init__(self, distance, playTye, cardsInPlay, cardsMissing):
        self.distance = distance
        self.playType = playType
        self.cardsInPlay = cardsInPlay

def pairDistance(cardsOnTable, cardsNotShown):
    plays = []
    for cardOne in cardsOnTable:
        for cardTwo in cardsNotShows:
            if cardOne.number == cardTwo.number:
                plays.append( Play(0, "PAIR" , [cardOne, cardTwo]) )
            else:
                plays.append( Play(1, "PAIR", [cardOne]) )
                plays.append( Play(1, "PAIR", [cardTwo]) )
    return plays

def twoCardsPlay(cardsOnTable, cardsNotShown):
    for cardOne in cardsOnTable:
        for i in range(len(cardsNotShown)):
            cardTwo = cardsNotShown[i]
                
def threeCardsPlay(cardsOnTable, cardsNotShown):
    for cardOne in cardsOnTable:
        for i in range(len(cardsNotShown)):
            cardTwo = cardsNotShown[i]
            for j in range(i + 1, len(cardsNotShown)):
                cardThree = cardsNotShown[j]

def fourCardsPlay(cardsOnTable, cardsNotShown):
    for cardOne in cardsOnTable:
        for i in range(len(cardsNotShown)):
            cardTwo = cardsNotShown[i]
            for j in range(i + 1, len(cardsNotShown)):
                cardThree = cardsNotShown[j]
                for k in range(j + 1, len(cardsNotShown)):
                    cardFour = cardsNotShown[k]
                

def calculatePlay(cards, playType):
    if playType == "PAIR"
        if len(cards) != 2:
            pass


        
    
