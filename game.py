from deck import Deck, Card


class Hand:
    def __init__(self, deck):
        """
        Draws 5 cards from the given deck to create a poker hand.

        Args:
            deck (Deck): The deck to deal cards from.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Returns the list of Card objects in the hand.

        Returns:
            list of Card: The current 5-card poker hand.
        """
        return self._cards

    @property
    def is_flush(self):
        """
        Determines whether all cards in the hand share the same suit.

        Returns:
            bool: True if all cards are of the same suit (flush), False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    def __str__(self):
        """
        Returns a string representation of the hand, showing all 5 cards.

        Returns:
            str: A string showing the cards in the hand.
        """
        return str(self._cards)

    @property
    def num_matches(self):
        """
        Calculates the total number of matching rank pairs among the 5 cards.
        Used to detect combinations like pairs, two pairs, etc.

        Returns:
            int: The count of rank matches (for example, 12 for four of a kind, 8 for full house).
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if the hand contains exactly one pair (two cards of the same rank).

        Returns:
            bool: True if the hand is a pair, False otherwise.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        if matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        """
        Checks if the hand contains exactly two pairs (two sets of two cards of the same rank).

        Returns:
            bool: True if the hand is two pair, False otherwise.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        if matches == 4:
            return True
        return False

    @property
    def is_quads(self):
        """
        Checks if the hand contains four cards of the same rank (four of a kind).

        Returns:
            bool: True if the hand is four of a kind, False otherwise.
        """
        if self.num_matches == 12:
            return True
        else:
            return False

    @property
    def is_full_house(self):
        """
        Checks if the hand contains a full house (three of a kind + a pair).

        Returns:
            bool: True if the hand is a full house, False otherwise.
        """
        if self.num_matches == 8:
            return True
        else:
            return False

    @property
    def is_straight(self):
        """
        Checks if the hand contains five cards in consecutive rank order (no duplicates).
        Note: Ace-high and ace-low straights are not handled.

        Returns:
            bool: True if the hand is a straight, False otherwise.
        """
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != Card.RANKS.index(self.cards[0].rank) + 4:
            return False
        return True


matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        print(hand)
        matches += 1
        break
print(f"The probability of a straight is {100 * matches / count}%")

