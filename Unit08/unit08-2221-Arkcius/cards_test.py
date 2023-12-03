"""
Purpose to test cards py function
Author: Ryan Robison
"""

import cards

def test_single():
    tester = cards.make_card(2,"Hearts")
    expected = (2, 'Hearts', '2 of Hearts', '\x1b[31m 2H\x1b[37m')
    assert tester == expected
def test_ten():
    tester = cards.make_card(10,"Spades")
    expected = (10, 'Spades', '10 of Spades', '\x1b[34m10S\x1b[37m')
    assert tester == expected
def test_jack():
    tester = cards.make_card(11,"Diamonds")
    expected = (11, 'Diamonds', 'Jack of Diamonds', '\x1b[31m JD\x1b[37m')
    assert tester == expected
def test_queen():
    tester = cards.make_card(12,"Clubs")
    expected = (12, 'Clubs', 'Queen of Clubs', '\x1b[34m QC\x1b[37m')
    assert tester == expected
def test_king():
    tester = cards.make_card(13,"Clubs")
    expected = (13, 'Clubs', 'King of Clubs', '\x1b[34m KC\x1b[37m')
    assert tester == expected
def test_ace():
    tester = cards.make_card(14,"Clubs")
    expected = (14, 'Clubs', 'Ace of Clubs', '\x1b[34m AC\x1b[37m')
    assert tester == expected

def test_deck():
    tester = cards.make_deck()
    expected = cards.make_card(2,"Clubs")
    assert tester[0] == expected
def test_deck():
    tester = cards.make_deck()
    expected = cards.make_card(2,"Diamonds")
    assert tester[13] == expected
def test_deck():
    tester = cards.make_deck()
    expected = cards.make_card(2,"Hearts")
    assert tester[27] == expected
def test_deck():
    tester = cards.make_deck()
    expected = cards.make_card(2,"Spades")
    assert tester[39] == expected