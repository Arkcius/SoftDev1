"""
more practice
Author:Ryan Robison
"""
import arrays
import math
#finds all numbers through n that are divisible by 5 xor 3
def divis(n,list0=[]):
    #if n is 3 or less adds 3 to list and returns list
    if n <= 3:
        list0.append(3)
        return list0
    #else
    else:
        #if its divisble by 3 and 5 then checks with another if to see if its only by one
        if n%3 == 0 or n%5 == 0:
            if n%3 != n%5:
                #calls next divis for number less then appends number
                divis(n-1,list0)
                list0.append(n)
            #else for both is calls next smaller number
            else:
                divis(n-1,list0)
        else:
            divis(n-1,list0)
    #return
    return list0

#takes in file letter and number and returns array of first number of words to start with letter
def find_words(filename,letter,number):
    #opens file
    with open(filename) as file:
        #starts count at 0 and makes empty list
        count = 0
        list0 = []
        #for line in file splits line
        for line in file:
            liner = line.split()
            #for element in split line
            for element in liner:
                #checks if count is < number
                if count < number:
                    #if the first letter of the element is the letter makes addd = true
                    if element[0].lower() == letter:
                        addd = True
                        #checks and if the word is already in list0 makes addd false
                        if len(list0) > 0:
                            for i in range(len(list0)):
                                if element == list0[i]:
                                    addd = False
                        #if addd is true by time hits here adds word to list and increases count
                        if addd == True:
                            list0.append(element)
                            count += 1
        #makes an array to length of list and then adds all elements of list to it and returns array
        ray = arrays.Array(len(list0))
        for i in range(len(list0)):
            ray[i] = list0[i]
        return ray   

#takes in starting weekday and total days and returns 2d list of calender
def calender(weekday,days):
    #makes current day and empty calender
    current = 1
    calenderr = []
    #calculates nummber of weeks needed
    weeks = math.ceil((days+weekday)/7)
    #makes empty week listsf
    for i in range(weeks):
        calenderr.append([])
    #while current day <= total days
    while current <= days:
        #checks to see if the length of the first week is less than starting day and if so adds empty string
        while len(calenderr[0]) < weekday:
            calenderr[0].append("  ")
        #while first week is less than 7 adds days
        while len(calenderr[0]) < 7:
            #if day is less than 10 adds the zero
            if current < 10:
                day = "0"+str(current)
            #else just makes it a string
            else:
                day = str(current)
            #adds day to week and ups current day
            calenderr[0].append(day)
            current += 1
        #goes through rest of the weeks
        for i in range(len(calenderr)-1):
            #while week less than 7
            while len(calenderr[i+1]) < 7:
                #checks to make sure current isnt over days
                if current <= days:
                    #same number check as for first week
                    if current < 10:
                        day = "0"+str(current)
                    else:
                        day = str(current)
                    #adds to current and appends to week
                    current += 1
                    calenderr[i+1].append(day)
                else:
                    #else if already maxed on days adds blanks till 7 week slots
                    while len(calenderr[-1]) < 7:
                        calenderr[-1].append("  ")
    #returns calender
    return calenderr

                        

def main():
    print(divis(20))
    ray = find_words("data/atotc.txt","a",5)
    print(ray)
    weeks = math.ceil((31+0+1)/7)
    print(weeks)
    calenderr = calender(2,31)
    for i in range(len(calenderr)):
        print(calenderr[i])

main()