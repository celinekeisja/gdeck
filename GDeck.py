
class Card:
    """Card class that has user-defined suit and rank."""
    def __init__(self, suit, rank):
        """Define a Card object that has a suits and ranks."""
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """Return the suit and rank of the Card."""
        return f'{self.rank} of {self.suit}'


class Deck:
    """Deck class that contains objects from the Card class."""
    suits = ['Diamonds', 'Hearts', 'Spades',  'Clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self):
        """Instantiate a deck that has card objects."""
        self.cards = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]
        self.ctr = 0

    def __iter__(self):
        """__iter__ to make the Deck class iterable."""
        return self

    def __next__(self):
        """Identify the next card in the deck in order."""
        if self.ctr >= len(self.cards):
            raise StopIteration
        card = self.cards[self.ctr]
        self.ctr += 1
        return card

    def __getitem__(self, index):
        """Get the identity of the card in the defined index."""
        return self.cards[index]

    def __len__(self):
        """Get the length of the deck."""
        return len(self.cards)

    def __repr__(self):
        """Identify that the object is a 'Deck of cards'."""
        return str(self.cards)
