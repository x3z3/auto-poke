import cardrules as cr

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.hand = cr.Hand()

    def __str__(self):
        return str(self.id) + self.name + '\n' + str(self.hand)

class PokerGame:
    def __init__(self, num_players, names=None):
        if num_players < 2:
            raise Exception('Not enough players')
        
        self.num_players = num_players
        self.players = []
        self.deck = cr.Deck()
        self.wild_pile = cr.Pile()

        if names is None:
            names = ['Player ' + str(i) for i in range(1, num_players + 1)]
        
        for i in range(self.num_players):
            self.players.append(Player(names[i], i))
        
    
    def shuffle(self):
        self.deck.shuffle()
    
    # Deal cards to each player default:2 for poker
    def deal(self, rounds=2):
        for _ in range(rounds):
            for player in self.players:
                player.hand.add(self.deck.deal())

    # Burns the top card and puts it at the bottom of the deck
    def burn(self):
        self.deck.retrieve(self.deck.deal())

    # Puts cards from the deck into the wildcard set default:1 for Flop and River
    def reveal_card(self, rounds=1):
        for _ in range(rounds):
            self.wild_pile.add(self.deck.deal())
    
    def flop(self):
        self.burn()
        self.reveal_card(3)
    
    def turn(self):
        self.burn()
        self.reveal_card(1)

    def river(self):
        self.burn()
        self.reveal_card(1)
    
    def show_revealed_cards(self):
        print('Revealed cards:')
        for card in self.wild_pile.cards:
            print(card)

    def evaluate_hand(hand, wildcard_pile):
        pass
        