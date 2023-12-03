"""
Purpose to test guessing.py with pytest
Author: Ryan Robison
"""
import guessing
import random

#test function to test out or range below
def test_check_guess_less_than_1():
    #setup
    answer = 5
    guess = -1
    expected = "Out of Range"

    #invoke
    actual = guessing.check_guess(answer, guess)

    #analyze
    assert actual == expected

#test function to test out or range above
def test_check_guess_more_than_10():
    #setup
    answer = 5
    guess = 11
    expected = "Out of Range"

    #invoke
    actual = guessing.check_guess(answer, guess)

    #analyze
    assert actual == expected

#test function to test too low
def test_check_guess_low():
    #setup
    answer = 5
    guess = 2
    expected = "Too low"

    #invoke
    actual = guessing.check_guess(answer, guess)

    #analyze
    assert actual == expected

#test function to test too high
def test_check_guess_high():
    #setup
    answer = 5
    guess = 7
    expected = "Too high"

    #invoke
    actual = guessing.check_guess(answer, guess)

    #analyze
    assert actual == expected

#test function to test correct
def test_check_guess_correct():
    #setup
    answer = 5
    guess = 5
    expected = "Correct"

    #invoke
    actual = guessing.check_guess(answer, guess)

    #analyze
    assert actual == expected

#main generates random int and then asks player to input guess till either they get it or they try 3 times
def main():
    #generates the answer then asks for first guess
    answer = random.randint(1,10)
    guess = int(input("Enter your Guess: "))
    #uses guessing.check_guess to check if the answer was correct or not
    checker = guessing.check_guess(answer,guess)
    #is a counter to make sure guesses dont go over 3
    count = 1
    print(checker)
    #if statment that checks if checker was not correct and count less than 3
    if checker != "Correct" and count < 3:
        #does the same as the original ask and check except now count is count +1 to keep a running tally
        guess = int(input("Enter your Guess: "))
        checker = guessing.check_guess(answer,guess)
        count = count + 1
        print(checker)
        #again checks if checker was not correct and count less than three
        if checker != "Correct" and count < 3:
            #same as previous if statment
            guess = int(input("Enter your Guess: "))
            checker = guessing.check_guess(answer,guess)
            count = count + 1
            print(checker)
    #prints game over at the end
    print("Game Over")


main()
