"""
Purpose to practice old codes
Author: Ryan Robison
"""

import csv

#finds street
def find_streets(filename,street):
    #opens file and makes it csv reader
    with open(filename) as filer:
        file = csv.reader(filer)
        next(file)
        #count is false until atleast 1 found
        count = False
        for line in file:
            #goes through every line and sees if matches and if so makes count true and prints
            if line[0] == street.upper():
                count = True
                print(line)
        #if not found prints false4
        if count == False:
            print("No Streets Found")

#finds the max for a streets name
def max_street(filename,street):
    #opens file as csv
    with open(filename) as filer:
        file = csv.reader(filer)
        next(file)
        #count starts at 0
        count = 0
        #for every line if the street name is found again increases count
        for line in file:
            if line[0] == street.upper():
                count += 1
        #returns count
    return count

    #finds the max street
def maxxer_street(filename):
    with open(filename) as filer:
        file = csv.reader(filer)
        next(file)
        #open file above and below makes bas for max and maxcount
        maxxcount = 0
        maxed = ""
        #goes through every line and then chechs if the maxx from that street name is bigger than the max being held
        for line in file:
            maxx = max_street(filename,line[0])
            if maxx >= maxxcount:
                maxxcount = maxx
                maxed = line[0]
        return maxed,maxxcount
        #

def main():
    find_streets("data/streets.csv","mission bay")
    street,count = maxxer_street("data/streets.csv")
    print(street, " appeared ",count," times")


main()