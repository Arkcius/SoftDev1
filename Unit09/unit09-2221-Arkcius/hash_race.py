"""
purpose to make different hash functions and see whats fastest
Author: Ryan Robison
"""
import time

#hashes using only first character
def hash_first_char(string = None):
    #if string is empty or no string given return 0
    if string == None or string == "":
        return 0
    else:
        #otherwise return the string of the first characters hash
        a = string[0]
        return ord(a)

#hashing using all characters weighted equally
def hash_sum(string = None):
    #if string is none or empty then return 0
    if string == None or string == "":
        return 0
    #otherwise starts sum at 0
    else:
        sum = 0
        #and for each character in string adds its hash value to the sum and returns sum
        for i in range(len(string)):
            sum += ord(string[i])
        return sum

#hash using weighted values for each string
def hash_positional_sum(string = None):
    #if string is none or empty return 0
    if string == None or string == "":
        return 0
    #otherwise start sum
    else:
        sum = 0
        #for every character does the hash of the character times the 31 to the power of the length minus index + 1
        for i in range(len(string)):
            sum += ord(string[i])*31**(len(string)-(i+1))
        return sum

#builds the collision counter
def build_collision_counter(hashing):
    #opens file
    with open("data/long_line_words.txt") as filename:
        #makes empty dictionary
        colcount = dict()
        #for every line in file 
        for line in filename:
            #trys to add one if it already exists
            try:
                colcount[hashing(line)] = colcount[hashing(line)]+1
            #otherwise if theres a key error aka it doesnt exist makes it set to 1
            except KeyError:
                colcount[hashing(line)] = 1
        return colcount

#tests the hashing
def hash_test(colcount,hashing):
    #gets the name of the function
    name = hashing.__name__
    sum = 0
    #makes a sum and goesthrough every element in the dictionary to add them to the sum
    for element in colcount:
        sum += colcount[element]
    #makes the ratio by sum - number of keys divided by sum then rounds it
    ratio = round((sum-len(colcount))/sum * 100,2)
    #gets the max value -1
    maxx = max(colcount.values()) -1
    #does length divided by sum to get the spread
    spread = round(len(colcount)/sum * 100,2)
    #times how long function takes to run
    start = time.perf_counter()
    result = build_collision_counter(hashing)
    end = time.perf_counter()
    #speed is end-start
    speed = round(end - start,2)
    #prints all info
    print("Hash Function", name)
    print("Total Collision Rate: ", ratio, "%", sep="")
    print("Maximum Collision: ",maxx)
    print("Spread: ",spread,"%",sep = "")
    print("Speed: ",speed,"seconds")
    print()

def main():
    colcount = build_collision_counter(hash)
    hash_test(colcount,hash)
    colcount = build_collision_counter(hash_first_char)
    hash_test(colcount,hash_first_char)
    colcount = build_collision_counter(hash_sum)
    hash_test(colcount,hash_sum)
    colcount = build_collision_counter(hash_positional_sum)
    hash_test(colcount,hash_positional_sum)

main()