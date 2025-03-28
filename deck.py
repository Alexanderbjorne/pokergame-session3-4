import random

class Card:
    """
    Represents a single playing card with a rank and suit.
    Supports comparison and string representation.
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "K", "A"]
    SUITS = ["♥️", "♦️", "♣️", "♠️"]  # Hearts, Diamonds, Clubs, Spades

    def __init__(self, rank, suit):
        """
        Initializes a Card with the given rank and suit.

        Args:
            rank (str): The rank of the card (e.g., 'A', '10', 'K').
            suit (str): The suit symbol of the card (e.g., '♠️').

        Raises:
            ValueError: If the rank or suit is invalid.
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Returns the rank of the card.

        Returns:
            str: Card rank.
        """
        return self._rank

    @property
    def suit(self):
        """
        Returns the suit of the card.

        Returns:
            str: Card suit.
        """
        return self._suit

    def __str__(self):
        """
        Returns a human-readable string representation of the card.

        Returns:
            str: e.g., 'Q♠️'
        """
        return f"{self._rank}{self._suit} "

    def __repr__(self):
        """
        Returns the official string representation of the card (same as __str__).

        Returns:
            str: e.g., 'Q♠️'
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Checks if two cards have the same rank.

        Args:
            other (Card): The card to compare with.

        Returns:
            bool: True if ranks are equal.
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Compares cards based on rank (ignoring suit).

        Args:
            other (Card): The card to compare with.

        Returns:
            bool: True if self is lower in rank than other.
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    """
    Represents a standard 52-card deck.
    Supports shuffling, dealing, and viewing the cards.
    """
    def __init__(self):
        """
        Initializes a new deck with 52 unique Card objects.
        """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """
        Returns the list of remaining cards in the deck.

        Returns:
            list of Card: Cards left in the deck.
        """
        return self._cards

    def __str__(self):
        """
        Returns a string showing all remaining cards in the deck.

        Returns:
            str: The deck as a list of cards.
        """
        return str(self._cards)

    def shuffle(self):
        """
        Randomly shuffles the order of cards in the deck.
        """
        random.shuffle(self._cards)

    def deal(self):
        """
        Removes and returns the top card from the deck.

        Returns:
            Card: The dealt card.
        """
        return self._cards.pop(0)

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)
