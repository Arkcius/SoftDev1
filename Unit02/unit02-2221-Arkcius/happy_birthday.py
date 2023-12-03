"""
This code prompts user to input name and birthday and returns it in a message
Author: Ryan Robison
"""
def birth():
    #func that gets input of name and birthday then prints it
    name = input("Enter your name: ")
    birth_m = input("Enter your birth month: ")
    birth_d = input("Enter your birth day: ")
    birth_y = input("Enter your birth year: ")
    print(name, "your birthday is on",birth_m, birth_d,",",birth_y)

birth()