"""
Purpose to make a card game called idiots delight
Author: Ryan Robison
"""
import cards

#deals a hand and makes a deck
def deal_hand():
    #makes a deck and shuffles it
    deck = cards.make_deck()
    cards.shuffle(deck)
    #deals a hand of 4 cards
    hand = cards.deal_one_hand(deck,4)
    #returns dexk and hand
    return deck,hand

#discards cards 
def discard(hand,number):
    #if the length of hand less than 4 or the number isnt 2 or 4 returns hand
    if len(hand)<4 or not(number ==2 or number == 4):
        return hand
    #otherwise
    else:
        #if number = 4 takes away last 4 cards
        if number == 4:
            for _ in range(4):
                hand.pop()
        #if number = 2 takes away second to last and third to last card 
        if number == 2:
            for _ in range(2):
                ind = len(hand)
                hand.pop(ind-2)

#function to print hand
def phand(hand):
    for i in range(len(hand)):
            print(hand[i][3],end =" ")
    print()

#function to play a round
def play_round(deck,hand):
    #if hand less than 4 cards draws until 4 cards
    if len(hand) < 4:
        while len(hand)<4:
            if len(deck)== 0:
                break
            cards.draw(deck,hand) 
    #wwhile hand length >= 4
    while len(hand)>=4 or deck == 0:
        #if length of the deck is more than 0 draws a card and prints hand
        if len(deck)>0:
            cards.draw(deck,hand)
        if len(deck)<3:
            phand(hand)
        #makes and ind for last index value
        ind = len(hand)-1
        #if last index and 4th to last index have same rank then discard 4 and continue
        if hand[ind][0] == hand[ind-3][0]:
            discard(hand,4)
            continue
        #else if 2nd and 3rd to last have same suit discard 2 and continue
        elif hand[ind-1][1] == hand[ind-2][1]:
            discard(hand,2)
            continue
        #else retunr deck and hand
        else:
            return deck,hand

def main():
    tries = 0
    ty = True
    while ty == True:
        #makes and deck and starting hand and prints hand
        deck,hand = deal_hand()
        phand(hand)
        #while cards still in deck plays rounds
        while len(deck)>0:
            play_round(deck,hand)
        #if at the end hand length = 0 you win
        if len(hand) == 0:
            print("you win")
            print("Tries:",tries)
            ty = False
            break
        #otherwise you lose and it says your score and nice try
        else:
            phand(hand)
            print(tries)

            tries += 1 


main()