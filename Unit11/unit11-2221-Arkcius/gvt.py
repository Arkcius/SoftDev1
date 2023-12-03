import random
import goatils
COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

GOATS = "Goats"
TROLLS = "Trolls"

TROLL_NAMES = ["Troll","Trollington","Trolizord"]

class Card:
    __slots__ = ["__name","__cost","__rarity",
    "__faction","__ap","__health"]

    def __init__(self,name,rarity,cost,faction,ap,health):
        self.__name = name
        self.__cost = cost
        self.__rarity = rarity
        self.__faction = faction
        self.__ap = ap
        self.__health = health
    
    def get_name(self):
        return self.__name
    def get_cost(self):
        return self.__cost
    def get_rarity(self):
        return self.__rarity
    def get_faction(self):
        return self.__faction
    def get_attack(self):
        return self.__ap
    def get_health(self):
        return self.__health

    def __repr__(self):
        output = self.__name \
        + "\nRarity: " + str(self.__rarity) \
        + "\nFaction: " + self.__faction \
        + "\nResource Cost: " + str(self.__cost) \
        + "\nHealth Points: " + str(self.__health) \
        + "\nAttack Power: " + str(self.__ap)
        return output

    def __str__(self):
        return "[" + self.__faction[0] + self.__name[0] \
            + " " + "{:02d}".format(self.__cost) \
            + " " + "{:02d}".format(self.__ap) \
            + " " + "{:02d}".format(self.__health) \
            + "]"
    
    def damage(self,damage):
        if damage <= self.__health:
            self.__health -= damage
            return 0
        else:
            current = self.__health
            self.__health = 0
            return damage - current
    def is_conscious(self):
        return self.__health>0

    def __eq__(self,other):
        if type(self) == type(other):
            return self.__rarity == other.__rarity \
                and self.__faction == other.__faction \
                and self.__cost == other.__cost \
                and self.__ap == other.__ap
        else:
            return False
    
    def __lt__(self,other):
        if self.__cost != other.__cost:
            return self.__cost < other.__cost
        else:
            return self.__name < other.__name

def make_card(faction,rarity):
    name = ""
    if faction == GOATS:
        name = goatils.make_goat_name()
    else:
        randex = random.randrange(len(TROLL_NAMES))
        name = TROLL_NAMES[randex]
    
    total = 0
    cost = 0
    if rarity == COMMON:
        total = 8
        cost = random.randint(1,3)
    elif rarity == UNCOMMON:
        total = 12
        cost = random.randint(2,5)
    elif rarity == RARE:
        total = 16
        cost = random.randint(4,7)
    elif rarity == LEGENDARY:
        total = 24
        cost = 10
    else:
        raise ValueError("Invalid card rarity: "+str(rarity))
    
    health = random.randint(1,total)
    ap = total - health

    return Card(name,rarity,cost,faction,ap,health)

def make_deck(faction):
    deck = []
    for i in range(20):
        deck.append(make_card(faction, COMMON))
    for i in range(10):
        deck.append(make_card(faction, UNCOMMON))
    for i in range(8):
        deck.append(make_card(faction, RARE))
    for i in range(2):
        deck.append(make_card(faction, LEGENDARY))
    random.shuffle(deck)
    return deck

class Player:
    __slots__ =["__name","__score","__maxrp","__rp","__deck","__hand","__battalion","__graveyard"]

    def __init__(self,name,deck):
        self.__name = name
        self.__score = 20
        self.__maxrp = 0
        self.__rp = 0
        self.__deck = deck
        self.__hand = []
        self.__battalion = []
        self.__graveyard = []
        for _ in range(5):
            self.__hand.append(self.__deck.pop())
        self.__hand.sort()

    def get_score(self):
        return self.__score
    def get_deck_len(self):
        return len(self.__deck)
    def __str__(self):
        return "Player: "+self.__name
    
    def __repr__(self):
        output = "Player: " + self.__name \
            + "\nScore: " + str(self.__score) \
            + "\nResource Points: " + str(self.__rp) + "/" + str(self.__maxrp) \
            + "\nDeck: " + str(len(self.__deck)) \
            + "\nGraveyard: " + str(len(self.__graveyard))
        output += "\nBattalion: "
        for card in self.__battalion:
            output += str(card) + " "
        output += "\nHand: "
        for card in self.__hand:
            output += str(card) + " "
        return output
    
    def start_turn(self):
        if self.__maxrp < 10:
            self.__maxrp += 1
        self.__rp = self.__maxrp
        if len(self.__deck) > 0:
            card = self.__deck.pop()
            self.__hand.append(card)
            self.__hand.sort()

    def play_card(self,number):
        if len(self.__hand) > number:
            if self.__hand[number].get_cost() <= self.__rp:
                self.__rp -= self.__hand[number].get_cost()
                self.__battalion.append(self.__hand.pop(number))
                return True
        else:
            return False
                
    def get_totalap(self):
        total = 0
        for i in range(len(self.__battalion)):
                total += self.__battalion[i].get_attack()
        return int(total)
    def card_info(self,number):
        print(repr(self.__hand[number]))

    def bat_info(self):
        for i in range(len(self.__battalion)):
            print(repr(self.__battalion[i]))


    def attack(self,attack):
        while attack > 0 and len(self.__battalion) >0:
            if attack >= self.__battalion[len(self.__battalion)-1].get_health():
                attack -= self.__battalion[len(self.__battalion)-1].get_health()
                self.__battalion.pop(len(self.__battalion)-1)
            else:
                self.__battalion[len(self.__battalion)-1].damage(attack)
                attack = 0
        if attack > 0:
            self.__score -= attack
