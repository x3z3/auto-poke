import random

class Card:
    def __init__(self, rank, suit):
        # Check types of suit and rank
        if suit not in ['S', 'H', 'D', 'C']:
            raise ValueError('Invalid suit')
        if rank not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            raise ValueError('Invalid rank')

        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['S', 'H', 'D', 'C']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def retrieve(self, card):
        self.cards.append(card)

    def __str__(self):
        ret = ''
        for card in self.cards:
            ret += str(card) + '\n'
        ret += str(len(self.cards)) + ' cards in deck'
        return ret

d = Deck()
print(d)
