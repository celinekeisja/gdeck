from GDeck import *
import pytest

test_suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
test_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def test_card():
    test_card_class = Card('test_suit', 'test_rank')
    assert test_card_class.suit == 'test_suit'
    assert test_card_class.rank == 'test_rank'
    assert f'{test_card_class}' == 'test_rank of test_suit'


def test_deck():
    assert str(Deck()) == str([f'{rank} of {suit}' for suit in Deck.suits for rank in Deck.ranks])
    assert Deck.ranks == test_ranks
    assert Deck.suits == test_suits
    assert f'{Deck()[0]}' == 'Ace of Diamonds'
    assert f'{next(Deck())}' == f'{Deck.ranks[0]} of {Deck.suits[0]}'
    assert len(Deck()) == 52
    assert iter(Deck())
    with pytest.raises(StopIteration):
        deck = Deck()
        for i in iter(Deck()):
            next(deck)
        next(deck)



