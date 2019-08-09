class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __eq__(self, other):
        return self.number == other.number and self.suit == other.suit

    def __ne__(self, other):
        return self.number != other.number or self.suit != other.suit

    def __hash__(self):
        return hash((self.number, self.suit))

    
