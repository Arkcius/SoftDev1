"""
Purpose mini practicum 9
Author: Ryan Robison
"""

def make_letter_frequecy(filename):
    with open(filename) as file:
        alpha = dict()
        for line in file:
                for i in range(len(line)):
                    if line[i].upper() != line[i].lower():
                        try:
                            alpha[line[i].lower()] = alpha[line[i].lower()] + 1
                        except KeyError:
                            alpha[line[i].lower()] = 1
        return alpha
    
def print_letter_frequency(lettercount):
    string ="abcdefghijklmnopqrstuvwxyz"
    maxx = 0
    for i in range(len(string)):
        try:
            print(string[i],":",lettercount[string[i]])
            if lettercount[string[i]] > maxx:
                maxx = lettercount[string[i]]
                let = string[i]
        except KeyError:
            print(string[i],":",0)
    print("MAX",let,":",maxx)



def main():
    filename = '../data/alice.txt'
    #filename = '../data/rit_mission.txt'
    letter = make_letter_frequecy(filename)
    print_letter_frequency(letter)

main()