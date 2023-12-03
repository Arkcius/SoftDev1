"""
Make Pokemon
Author: Ryan Robison
"""

class Pokemon:
    __slots__ = ["__name","__type","__hp","__damage"]

    #init for all needed items
    def __init__(self,name:str,type:str,hp:int,damage:int) -> None:
        self.__name = name 
        self.__type = type
        self.__hp = hp 
        self.__damage = damage

    #returns damage
    def get_damage(self):
        return self.__damage

    #takes away damage from health
    def lose_round(self,damage):
        self.__hp -= damage

    #checks if hp is 0 or less and if so returns true
    def is_fainted(self):
        if self.__hp <= 0:
            return True
        else:
            return False
    
    #returns self.name for print
    def __str__(self):
        return self.__name

    #returns name:type:hp for needed print
    def __repr__(self):
        return self.__name+":"+self.__type+":"+str(self.__hp)

    #if type and hp both equal returns true otherwise false
    def __eq__(self,other):
        if type(self) == type(other):
            if self.__type == other.__type:
                return self.__hp == other.__hp
        else: 
            return False
    
    #if types equal then return true if self hp less than other hp
    def __lt__(self,other):
        if type(self) == type(other):
            if self.__type == other.__type:
                return self.__hp < other.__hp
            #otherwise checks if it loses element and if so returns true
            elif self.__type == "Fire" and other.__type == "Water":
                return True
            elif self.__type == "Water" and other.__type == "Grass":
                return True
            elif self.__type == "Grass" and other.__type == "Fire":
                return True
            else:
                return False
        else:
            return False
        
    #hash based of name
    def __hash__(self):
        return hash(self.__name)