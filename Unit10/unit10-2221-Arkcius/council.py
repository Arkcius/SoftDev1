"""
Make an alien council
Author: Ryan Robison
"""

import random

class Admin:
    #slots for admin and then initializes
    __slots__ = ["name","departments","region","languages",]
    def __init__(self,name:str,departments:list,region:str,languages:list):
        self.name = name
        self.departments = departments
        self.region = region
        self.languages = languages
        
class Council:
    #slots for council and randomly picks chief
    __slots__ = ["chief","admins"]
    def __init__(self,admins:list):
        self.chief = admins[(random.randint(0,len(admins)-1))]
        self.admins = admins
        
#constants for the departments languages and regions
DEPARTMENTS = ["Health","Defense","Finance","Attack"]
LANGUAGES = ["English","Alien"]
REGIONS = ["Faraway","Closeby"]

#prints the admins full info
def print_admin(admin):
    #prints name followed by region
    print(admin.name)
    print("Region: ",admin.region)
    #then for loops to print all departments and languages admins heads or knows
    print("Departments: ")
    for elements in admin.departments:
        print("\t",elements)
    print("Languages")
    for elements in admin.languages:
        print("\t",elements)
    
#print council prints just counselor names
def print_council(council):
    print("COUNCIL")
    #prints the chiefs name after printing CHIEF
    print("\t[CHIEF] ",council.chief.name)
    #then for the rest of the elements that arent the chief it prints their names
    for elements in council.admins:
        if elements != council.chief:
            print("\t",elements.name)

#finds head of a department and returns returns none if no one is assigned
#also when it said find specifc team admin i assumed that meant find admin incharge of said department
#the wording was a little weird
def find_admin(council,department):
    for elements in council.admins:
        #scans through council elements and every admins departments to find who matches with given department and then returns said admin
        for i in range(len(elements.departments)):
            if elements.departments[i] == department:
                return elements
    return None

#returns council chief
def find_chief(council):
    return council.chief

#prints all info of all admins
def print_all(council):
    #first prints chief 
    print("CHIEF")
    print_admin(council.chief)
    #then for the rest of the admins that arent the chief prints them out
    for elements in council.admins:
        if elements != council.chief:
            print()
            print_admin(elements)

def main():
    steve = Admin("Steve",[DEPARTMENTS[1]],REGIONS[1],[LANGUAGES[1]])
    #test print admin
    print_admin(steve)
    bob = Admin("Bob",[DEPARTMENTS[0]],REGIONS[1],[LANGUAGES[1]])
    joe = Admin("Joe",[DEPARTMENTS[2]],REGIONS[0],[LANGUAGES[0],LANGUAGES[1]])
    cy = Admin("Cy",[DEPARTMENTS[3]],REGIONS[1],[LANGUAGES[0]])
    council = Council([steve,bob,joe,cy])
    #test find chief
    print("CHIEF")
    print_admin(find_chief(council))
    print()
    #test find admin
    print("Head of",DEPARTMENTS[3])
    print_admin(find_admin(council,DEPARTMENTS[3]))
    print()
    #test print council
    print_council(council)
    print()
    #test print all
    print_all(council)

main()
