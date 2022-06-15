import cardrules as cr

deck = cr.Deck()
pile = cr.Pile()

pile.add(deck.deal())
pile.add(deck.deal())
pile.add(deck.deal())

pile.add(pile.remove())

print(pile)
