"""
Purpose to ask the person to input the correct number of pi
Author: Ryan Robison
"""

def pi_tester():
    #adds pi and makes pi a string
    pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    #sets variables to starting values
    correct = True
    ind = 2
    total = 0
    #while loop runs while correct == true
    while correct == True:
        #guess next number
        guess = (input("Enter the next decimal digit of pi:"))
        #and if the ind == lenpi-1 then thats all digits 
        if ind == len(pi)-1:
            print("All correct")
            total += 1
            return total
        #if input == pi of that index it adds 1 to index and total
        elif guess == (pi[ind]):
            ind +=1
            total +=1
        #else if it doesnt it prints correct answer and returns total
        elif guess != (pi[ind]):
            print("Correct answer:",(pi[ind]))
            return total


def display_score(score):
    if score <= 4:
        print("PI Neophyte")
    elif score <= 9:
        print("PI Novice")
    elif score <= 24:
        print("PI Journeyman")
    elif score <= 49:
        print("PI Enthusiast")
    elif score <= 96:
        print("PI Connoisseur")
    elif score <= 100:
        print("PI Expert")
    elif score > 100:
        print("PI imposter")
    print("Total Score:",score)

def main():
    display_score(pi_tester())


main()