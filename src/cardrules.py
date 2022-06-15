import random

class Card:
    def __init__(self, rank, suit):
        # Check types of suit and rank
        if suit not in ['S', 'H', 'D', 'C']:
            raise ValueError('Invalid suit')
        if rank not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            raise ValueError('Invalid rank')

        # Initializing class variables
        self.suit = suit
        self.rank = rank
    
    # Creates a string representation of the card
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['S', 'H', 'D', 'C']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(rank, suit))
                # Alternate code to explain the above line
                # card = Card(rank, suit)
                # self.cards.append(card)
    
    # Randomly shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Returns a single card from the top of the list
    def deal(self):
        return self.cards.pop()

    # Retrieves a single card to the end of the list
    def retrieve(self, card):
        self.cards.append(card)

    # Function to retrirve all cards, when a user returns a list of cards
    def retrieve_all(self, cards):
        for card in cards:
            self.retrieve(card)

    # Function to print a string version of the entire deck
    # USED FOR TESTING ONLY - The list should be hidden
    def __str__(self):
        ret = ''
        for card in self.cards:
            ret += str(card) + '\n'
        ret += str(len(self.cards)) + ' cards in deck'
        return ret


class Hand:
    def __init__(self):
        self.cards = []

    # Function to add a specific card to the hand
    def add(self, card):
        self.cards.append(card)
    
    # Function to remove a specific card from the hand, Does nothing if the card is not present
    def remove(self, suit, rank):
        for card in self.cards:
            if card.suit == suit and card.rank == rank:
                self.cards.remove(card)
                return card
    
    # Remove all cards, so you can clear the hand, and you can return hand to the deck
    def remove_all(self, suit):
        cards = []
        for card in self.cards:
            if card.suit == suit:
                cards.append(card)
        for card in cards:
            self.cards.remove(card)
        return cards

    # Function to print the current hand
    def __str__(self):
        ret = ''
        for card in self.cards:
            ret += str(card) + '\n'
        ret += str(len(self.cards)) + ' cards in hand'
        return ret

# Playfield testing
h = Hand()
d = Deck()
d.shuffle()


