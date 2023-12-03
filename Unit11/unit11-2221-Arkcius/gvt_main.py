"""
make the gvt game main
Author: Ryan Robison
"""
import gvt

def main():
    deck = gvt.make_deck("Trolls")
    player = gvt.Player("Howdy",deck)
    print(repr(player))
    player.start_turn()
    player.start_turn()
    player.play_card(0)
    print(repr(player))

main()

