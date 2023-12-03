"""
Make da pokemon fight
Author: Ryan Robison
"""
import pokedex

#battle the two partys
def battle(party1,party2):
    #starts at round 1
    round = 1
    #while true
    while True:
        #print round and remaining parties
        print("Round: ",round)
        print("Party1: ",party1)
        print("Party2: ",party2)
        #take pokemon from parties
        poke1 = party1.pop()
        poke2 = party2.pop()
        #compares if they equal and if so says draw and readds them to sets
        if poke1 == poke2:
            print(poke1," and ",poke2," battle to a draw")
            party1.add(poke1)
            party2.add(poke2)
        #if poke1 loses to poke2 then says who one and poke1 takes damage according to poke2 damgage
        elif poke1 < poke2:
            print(poke2, "has won the round over",poke1)
            poke1.lose_round(poke2.get_damage())
            party2.add(poke2)
            #then checks if loser fainted
            if poke1.is_fainted() == True:
                print(poke1," has fainted")
            else:
                party1.add(poke1)
        #same as above but if poke 2 loses
        elif poke2 < poke1:
            print(poke1, "has won the round over",poke2)
            poke2.lose_round(poke1.get_damage())
            party1.add(poke1)
            if poke2.is_fainted() == True:
                print(poke2," has fainted")
            else:
                party2.add(poke2)
        #if a party is less than or equal to 0 other wins and breaks loop
        if len(party2) <= 0:
            print("Winning party: ",party1)
            break
        elif len(party1) <= 0:
            print("Winning party: ",party2)
            break
        #adds to round and enter to stop each round
        round += 1
        next = input("Enter to continue")

def main():
    #main
    dex = pokedex.Pokedex()
    dex.load("data/pokemon.csv")
    party1,party2 = dex.create_parties()
    battle(party1,party2)

main()