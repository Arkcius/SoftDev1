""" Variable program to test variables
Author: Ryan Robison
"""
def variable_practice():
    #first variables
    age = 12*19+9
    day_year = 365
    pet = "Maverick"
    pi = 3.14159
    print(age,day_year,pet,pi)

#adding more variables of different types/using different opperations
def expressions_practice():
    literal = 12
    addition = 5+4
    exponent = 2**3
    floor = 5//2
    mod = 34%5
    para = (3+1)*4
    print(literal,addition,exponent,floor,mod,para)

#added prompt and print section to get two numbers from user and then do all basic operations on them
def prompt_and_print():
    revice = int(input("Enter a number: "))
    geats = int(input("Enter a second number: "))
    print(revice+geats)
    print(revice-geats)
    print(revice*geats)
    print(revice/geats)

def main():
    prompt_and_print()
    variable_practice()
    expressions_practice()

main()
