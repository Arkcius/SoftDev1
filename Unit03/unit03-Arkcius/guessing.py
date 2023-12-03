"""
Purpose of the program is to make a guessing game
Author: Ryan Robison
"""

#function that takes answer and guess and checks if its right or wrong and then returns a string on if it was correct,too high/low, or out of range
def check_guess(answer,guess):
    #if statment to see if guess is out of range
    if guess < 1 or guess > 10:
        return "Out of Range"
    #if statment to check if guess too high and return too high if it is
    if guess > answer:
        return "Too high"
    #if statment to check if guess too low and return too low if it is
    if guess < answer:
        return "Too low"
    #if statment to check and return if answer is correct
    if guess == answer:
        return "Correct"

