import random

class Card:
    def __init__(self, rank, suit):
        # Check types of suit and rank
        if suit not in ['S', 'D', 'C', 'H']:
            raise ValueError('Invalid suit')
        if rank not in range(1, 14):
            raise ValueError('Invalid rank')

        # Initializing class variables
        self.suit = suit
        self.rank = rank
        self.value,self.val = self.get_values()
        
    
    # Creates a string representation of the card
    def __str__(self):
        return self.val + ' of ' + self.suit

    # Returns the value of the card
    def get_values(self):
        if self.rank == 1:
            return 'Ace','A'
        elif self.rank == 10:
            return '10','T'
        elif self.rank == 11:
            return 'Jack','J'
        elif self.rank == 12:
            return 'Queen','Q'
        elif self.rank == 13:
            return 'King','K'
        else:
            return str(self.rank),str(self.rank)
    

class Deck:
    """
        Deck deals the top most face down card, and adds cards at the bottom of the pile
        
        Constructor initializes a deck of cards
        shuffle() shuffles the deck
        deal() deals the top most card face down card
        retrieve() retrieves a card and adds it to the bottom of the pile
        retrieve_all() retrieves a list of cards and adds them to the bottom of the pile
    """
    def __init__(self):
        self.cards = []
        for suit in ['S', 'D', 'C', 'H']:
            for rank in range(1, 14):
                self.cards.insert(0, Card(rank, suit))
                # Alternate code to explain the above line (Ignore the indentation, its only for demo)
                #                   card = Card(rank, suit)
                # self.cards.append(card)
    
    # Randomly shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Returns a single card from the top of the deck
    def deal(self):
        if len(self.cards) == 0:
            raise ValueError('No cards left in deck')
        return self.cards.pop(0)

    # Retrieves a single card to the bottom of a deck
    def retrieve(self, card):
        self.cards.append(card)

    # Function to retrieve all cards, when a user returns a list of cards
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


class Pile:
    """
        Pile is a resting spot for cards. Adds and removes cards from the top of the deck

        Constructor initializes a pile of cards to empty
        add() adds a card to the top of the pile
        remove() removes a card from the top of the pile
        clear() clears the pile and returns all the cards
    """
    def __init__(self):
        self.cards = []
    
    # Adds a card to the top of the pile
    def add(self, card):
        self.cards.append(card)
    
    # Removes a card from the top of the pile
    def remove(self):
        return self.cards.pop()
    
    # Clears the pile and returns all cards to the deck
    def clear(self):
        cards = self.cards
        self.cards = []
        return cards
    
    # Called by other functions to display the cards in the pile
    def return_cards(self):
        for card in self.cards:
            self.add(card)

    # For ease
    def __str__(self):
        ret = ''
        for card in self.cards:
            ret += str(card) + '\n'
        ret += str(len(self.cards)) + ' cards in pile'
        return ret


class Hand:
    """
        Hand is a class that represents a hand of cards.

        Constructor initializes a hand of cards to empty
        add() adds a card to the hand
        remove() removes a card from the hand
        clear() removes all cards from the hand

    """
    def __init__(self):
        self.cards = []

    # Function to add a specific card to the hand
    def add(self, card):
        self.cards.append(card)
    
    # Function to remove a specific card from the hand, Does nothing if the card is not present
    def remove(self, suit, value):
        for card in self.cards:
            if card.suit == suit and (card.value == value or card.val == value):
                self.cards.remove(card)
                return card
    
    # Remove all cards, so you can clear the hand, and you can return hand to the deck
    def clear(self, suit):
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