"""
Purpose to check if guess is right
Author: Ryan Robison
"""
import random

def is_correct(guess,answer):
    check = guess == answer
    return check

def check_guess(guess,answer):
    if guess == answer:
        return 0
    else:
        return None

def test_check_guess_correct():
    out = check_guess(5,5)
    assert (out == 0)

def main():
    answer = random.randint(1,10)
    guess = int(input("Enter guess: "))
    check = is_correct(guess,answer)
    print(check_guess(guess,answer))
    print(check)

main()