# Fluent Python Chapter One, example two
# review python collections and named tuples
import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """Pythonic card deck, demonstrates the power of implementing
    just two special methods, __getitem__ and __len__ (i.e. leveraging Python
    data model)
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        """For slicing"""
        return self._cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()
    print('Nr of cards in deck is', len(deck))
    print('The deck now supports slicing \n', deck[12::13])
    print('Gimme 2 random cards:', random.choice(deck), random.choice(deck))

    # the below in works because list is iterable (otw have to __contains__)
    print('Queen of hearts is in deck?', Card('Q', 'hearts') in deck)
    for card in deck[0:4]:
        print(card)
