# review python collections and namedtuples
import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    '''
    Pythonic card deck, demonstrates the power of implementing
    just two special methods, __getitem__ and __len__ (i.e. leveraging Python
    data model)
    '''
    # all cards from 2 to Ace in a list as ``class attributes``
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # protected attribute, list of namedtuple
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # for card shufflling (we can't now because of immutability)
    # def__setitem__():
    #   pass


if __name__ == '__main__':

    '''
    # Some training investigating the collections package
    # making a tuple more readable for the future us
    Color = collections.namedtuple('Color', ['red', 'green', 'blue'])
    white = Color(red=255, green=255, blue=255)

    # can also use subsetting: color[0]
    print(white.red, white.blue, white.green)

    l = ['a', 'a', 'b', 'c', 'c', 'c', 5]
    # extra things wrt dictionaries
    c = collections.Counter(l)
    # careful with negative counts, they dissappear
    print(c + collections.Counter(l))
    print(c.most_common())
    '''
    # note that a good practice is extracting statements from doctests

    deck = FrenchDeck()
    print('Nr of cards in deck is', len(deck))
    print('The deck now supports slicing \n', deck[12::13])
    print('Gimme 2 random cards:', random.choice(deck), random.choice(deck))

    # the below in works because list is iterable (otw have to __contains__)
    print('Queen of hearts is in deck?', Card('Q', 'hearts') in deck)
    for card in deck[0:4]:
        print(card)
