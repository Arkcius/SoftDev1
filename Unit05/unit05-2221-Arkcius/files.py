"""
Take in and print files
Author: Ryan Robison
"""

import plotter

def print_lines(filename):
    file = open(filename)
    for line in file:
        print(line)
    file.close()


def print_lines_a(filename):
    file = open(filename)
    for line in file:
        stripped = line.strip()
        print(stripped)
    file.close()

def word_search(filename):
    file = open(filename)
    word = input("Enter Word:")
    found = False
    for line in file:
        line2 = line.strip()
        if line2.lower() == word.lower():
            print("Found Word:",word)
            found = True
    if found != True:
        print("Didn't Find")
    file.close()

def longest_word(string):
    stripped = string.strip()
    longest_word = ""
    if stripped != "":
        words = stripped.split()
        for word in words:
            if len(word)> len(longest_word):
                longest_word = word
    print("Longest Word: ",longest_word)

def longest_words(filename):
    file = open(filename)
    for line in file:
        longest_word(line)
    file.close()


def print_names(filename):
    file = open(filename)
    next(file)
    for line in file:
        splited = line.split(",")
        print(splited[1],splited[0])
    file.close()

def calc(filename,col):
    with open(filename) as file:
        count = -1
        total = 0
        for line in file:
            splitted = line.split(",")
            if count < 0:
                typer = splitted[col]
            elif count>=0:
                total += float(splitted[col])
            count +=1
    print(typer,"average:",(total/count))


def plot_grades(filename,col):
    with open(filename) as file:
        header = next(file).split(",")
        name = header[col]
        plotter.init(name,"Persons","Score")
        for line in file:
            liner = line.split(",")
            grade = float(liner[col])
            plotter.add_data_point(grade)
        plotter.plot()
        


def main():
    #print_lines("data/numbers_01.txt")
    #print_lines_a("data/numbers_01.txt")
    #word_search("data/words.txt")
    #longest_words("data/alice.txt")
    #print_names("data/grades_010.csv")
    #calc("data/grades_010.csv",2)
    plot_grades("data/grades_010.csv",10)
    end = input("Enter to end:")
main()
