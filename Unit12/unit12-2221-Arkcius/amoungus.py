"""
make the who goes there game definetly not amoung us
Author: Ryan Robison
"""
import csv
import random

COLOR = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White", "Yellow"]
TURN = 0
TURN_TOTAL = 10
DONE = []

class Task:
    __slots__ = ["__name","__location"]

    def __init__(self,name,location):
        self.__name = name
        self.__location = location

    def get_name(self):
        return self.__name
    def get_location(self):
        return self.__location

    def __str__(self):
        return self.__name + " in " + self.__location

    def __lt__(self,other):
        if type(self) == type(other):
            return (len(self.__name)+len(self.__location)*3) < (len(other.__name)+len(other.__location)*3)


class Crew:
    __slots__ = ["__color","__tasks","__dead","__imposter"]

    def __init__(self,color):
        self.__color = color
        self.__tasks = []
        self.__dead = False
        self.__imposter = False

    def is_impost(self):
        return self.__imposter
    
    def imposterize(self):
        self.__imposter = True
    
    def get_tasks(self,value):
        return self.__tasks[value]

    def done(self):
        return self.__tasks == []
    
    def murder(self):
        self.__dead = True
    
    def isdead(self):
        return self.__dead

    def add_tasks(self,task):
        self.__tasks.append(task)

    def remove_task(self):
        self.__tasks.pop(0)

    def __lt__(self,other):
        if type(self) == type(other):
            return self.__dead <= other.__dead

    def __str__(self):
        if self.__dead == True:
            return self.__color + " Crewmate (deceased)"
        else:
            return self.__color + " Crewmate"

    def __repr__(self):
        output = "Crewmate \n\tColor = "+self.__color+"\n\tDead = "+str(self.__dead)+"\n\tTasks: ["
        for i in range(len(self.__tasks)-1):
            output += str(self.__tasks[i]) + ", "
        output += str(self.__tasks[len(self.__tasks)-1])
        output += "]"
        return output

class Ship:
    __slots__ = ["__tasks","__locations","__crew","__imposters","__done"]

    def __init__(self,value):
        with open("tasks_01.csv") as filer:
            file = csv.reader(filer)
            next(file)
            tasks = []
            locations = set()
            for line in file:
                tasks.append(Task(line[0],line[1]))
                locations.add(line[1])
        self.__tasks = tasks
        loc = []
        for elements in locations:
            loc.append(elements)
        self.__locations = loc
        crew,impost = make_crew(value)
        self.__crew = crew
        self.__imposters = impost
        self.__done = []
        for i in range(len(self.__crew)):
            give_tasks(self.__crew[i],self.__tasks)
    
    def get_loc(self):
        return self.__locations
    def loc(self,value):
        return self.__locations[value]
    def get_tasks(self):
        return self.__tasks
    def get_crew(self,value):
        return self.__crew[value]
    def get_impost(self):
        return self.__imposters
    def get_all(self):
        return self.__crew
    def get_done(self):
        return self.__done
    def add_done(self,crew):
        self.__done.append(crew)
    

def make_crew(value):
    global TURN_TOTAL
    global TURN
    if 1<=value<=4:
        Crewmates = []
        imposters = []
        TURN_TOTAL -= value
        for i in range(10):
            Crewmates.append(Crew(COLOR[i]))
        for _ in range(value):
            made = False
            while made == False:
                i = random.randint(0,9)
                if Crewmates[i].is_impost() == False:
                    Crewmates[i].imposterize()
                    made = True
                    imposters.append(Crewmates.pop(i))
        return Crewmates, imposters
    else:
        raise ValueError ("Imposter value out of range")

def give_tasks(crew,tasks):
    tasknum = random.randint(3,6)
    for _ in range(tasknum):
        j = random.randint(0,len(tasks)-1)
        crew.add_tasks(tasks[j])

def round(ship):
    global TURN,TURN_TOTAL
    imposterloc = []
    
    for i in range(len(ship.get_impost())):
        j = random.randint(0,len(ship.get_loc())-1)
        imposterloc.append(ship.loc(j))
    
    crew = ship.get_crew(TURN)
    turn1 = TURN
    donelen = ship.get_done()
    while True:
        for i in range(len(donelen)):
            if donelen[i] == crew:
                TURN = (TURN + 1) % TURN_TOTAL
                crew = ship.get_crew(TURN)
                if turn1 == TURN:
                    return False
                continue
            else:
                break
        else:
            try:
                task = crew.get_tasks(0)
            except:
                pass
            print(str(crew)+" begins "+str(task))
            for i in range(len(imposterloc)):
                murderer = False
                if task.get_location() == imposterloc[i]:
                    print("Imposter Murders "+str(crew))
                    crew.murder()
                    ship.add_done(crew)
                    murderer = True
                if murderer == True:
                    break
            if crew.isdead() == False:
                crew.remove_task()
                print("Task Complete")
                print(str(crew)," heads back to Cafeteria")
            if crew.done():
                ship.add_done(crew)

            TURN = (TURN + 1) % TURN_TOTAL
            return True

def print_remain(ship):
    crew = ship.get_all()
    for i in range(len(crew)):
        print(str(crew[i]))

def winner(ship):
    crew = ship.get_all()
    impostlose = False
    if len(ship.get_done()) == TURN_TOTAL:
        for i in range(len(crew)):
            if crew[i].isdead == False:
                impostlose = True
            print(crew[i])
    if impostlose == True:
        print("Journey End Crew made it")
    elif impostlose == False:
        print("Journey End Imposter Win")
    



                
            

def main():
        value = int(input("Enter Imposter Count "))
        while 4<value or value<1:
            print("Try Again")
            value = int(input("Enter Imposter Count "))
        shipper = Ship(value)
        rounder = True
        while rounder == True:
            rounder = round(shipper)
        
        

main()