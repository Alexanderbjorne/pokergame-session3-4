from deck import Deck, Card

class Hand:
    def __init__(self, deck):
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    @property
    def is_flush(self):  # ✅ Now inside the class
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    def __str__(self):
        return str(self._cards)

while True:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    if hand.is_flush:
        print(hand)
        break


