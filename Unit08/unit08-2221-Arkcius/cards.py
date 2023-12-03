"""
purpose to make a card tuple
Author: Ryan Robison
"""

import random

#function to take in rank and suit and return card tuple
def make_card(rank,suit):
    #s equals false for later error checking
    s = False
    #tuples of ranks and suits
    ranks = (2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace")
    suiters = ("Clubs","Diamonds","Hearts","Spades")
    #checks all elements in suiters to see if it matches a given suit and if not raises value erro
    for element in suiters:
        if suit == element:
            s = True
    if s == False:
        raise ValueError("Not an accepted Suit")
    #makes sure rank is in range or raises value error
    if rank < 2 or rank > 14:
        raise ValueError("Rank not Valid")
    #variable fro what the given rank is 
    ranker = ranks[rank-2]
    #sets name of card
    name = str(ranker)+" of "+suit
    #gets first letter of suit
    suits = suit[0]
    #if elif else statment to create the shorthands depending on what type of rank they are
    if rank < 10:
        shorthand = " "+ str(rank) + suits
    elif rank == 10:
        shorthand = str(rank) + suits
    else:
        shorthand = " " + ranker[0] + suits
    #checks if red card and then changes shorthand and else is blue card
    if suit == suiters[2] or suit == suiters[1]:
        shorthand = "\033[31m"+shorthand+"\033[37m"
    else:
        shorthand = "\033[34m"+shorthand+"\033[37m"
    #creates the tuple and returns it
    tuples = (rank,suit,name,shorthand)
    return tuples

#makes a deck of cards
def make_deck():
    deck = []
    #tuple of the suits
    suits = ("Clubs","Diamonds","Hearts","Spades")
    #for loop for all 4 types of suits with suit equaling current suit
    for j in range(4):
        suit = suits[j]
        #for loop for all ranks
        for i in range(13):
            #makes a card of current rank and suit and adds to deck
            card = make_card(i+2,suit)
            deck.append(card)
    #returns deck
    return deck

#shuffles deck
def shuffle(deck):
    #for all cards in the deck
    for ind in range(len(deck)):
        #finds a random card that is at a later index then itself
        swap = random.randint(ind,51)
        #then swaps them using a temp to store
        temp = deck[ind]
        deck[ind] = deck[swap]
        deck[swap] = temp
    #returns deck
    return deck

#function to draw a card and add it to ones hand
def draw(deck,hand):
    #if the deck is empty returns none
    if len(deck)<=0:
        return None
    #otherwise pops a card from the first slot and adds it to hand and returns popped card
    else:
        popper = deck.pop(0)
        hand.append(popper)
        return popper

#takes in a deck and amount of cards
def deal_one_hand(deck,cards):
    #sets i to 0 and makes an empty hand
    i = 0
    hand = []
    #while i is less than cards needed
    while i < cards:
        #draws a card and makes i go up
        draw(deck,hand)
        i += 1
    #returns hand
    return hand

def main():
    deck = make_deck()
    shuffle(deck)
    hand = deal_one_hand(deck,5)
    print(hand)
    for i in range(len(hand)):
        print(hand[i][3],end = " ")
    #previous tests below i thought id leave in
    """
    hand = []
    print(draw(deck,hand))
    print(hand)
    print(len(deck))
    print(deck[0])
    print(deck[13])
    print(deck[28])
    print(deck[51])
    print(deck[0],deck[3],deck[8])
    shuffle(deck)
    print(deck[0],deck[3],deck[8])
    card = make_card(2,"Hearts")
    print(card[3])
    """

if __name__ == "__main__":
    main()