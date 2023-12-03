"""
pokedex
Author: Ryan Robison
"""
import pokemon
import csv
import random

#slot for pokemon list
class Pokedex:
    __slots__ = ["__pokemon_list"]

    #init that makes empty list
    def __init__(self):
        self.__pokemon_list = []

    #loads with csv file all pokemon into its list
    def load(self,filename):
        with open(filename) as csv_file:
            file = csv.reader(csv_file)
            next(file)
            for line in file:
                self.__pokemon_list.append(pokemon.Pokemon(line[0],line[1],int(line[2]),int(line[3])))

    #creates party sets for each    
    def create_parties(self):
        party1 = set()
        party2 = set()
        #first party adds randomly until 6
        while len(party1) <= 6:
            party1.add(self.__pokemon_list[random.randint(0,len(self.__pokemon_list)-1)])
        while len(party2) <= 6:
            #second does the same but first checks if the pokemon is already in party 1 before adding
            i = random.randint(0,len(self.__pokemon_list)-1)
            if self.__pokemon_list[i] in party1:
                continue
            else:
                party2.add(self.__pokemon_list[i])
        #returns partys
        return party1, party2
