from GDeck import *
import pytest
import random

test_suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
test_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
test_card_class = Card('test_suit', 'test_rank')


def test_card_suit():
    """Test for the user defined suit."""
    assert test_card_class.suit == 'test_suit'


def test_card_rank():
    """Test for the user defined rank."""
    assert test_card_class.rank == 'test_rank'


def test_card_repr():
    """Test for the __repr__ of Card class."""
    assert f'{test_card_class}' == 'test_rank of test_suit'


def test_deck_repr():
    """Test for the __repr__ of Deck class."""
    assert str(Deck()) == str([Card(suit, rank) for suit in test_suits for rank in test_ranks])


def test_deck_rank():
    """Test for the ranks in the Deck class."""
    assert Deck.ranks == test_ranks


def test_deck_suit():
    """Test for the suits in the Deck class."""
    assert Deck.suits == test_suits


def test_deck_getitem():
    """Test for the __getitem__ of Deck class."""
    assert f'{Deck()[0]}' == 'Ace of Diamonds'


def test_deck_next():
    """Test for the __next__ of Deck class."""
    assert f'{next(Deck())}' == f'{test_ranks[0]} of {test_suits[0]}'


def test_deck_len():
    """Test for the __len__ of Deck class."""
    assert len(Deck()) == 52


def test_deck_iter():
    """Test for __iter__ and StopIteration in Deck class."""
    with pytest.raises(StopIteration):
        deck = Deck()
        for i in iter(Deck()):
            next(deck)
        next(deck)


def test_choice():
    """Test for the use of random.choice on Deck class."""
    assert isinstance(random.choice(Deck()), Card)
