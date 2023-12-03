"""
Purpose to test while loops
Author: Ryan Robison
"""

def countdown(number):
    summe = 0
    while number >= 0:
        print(number)
        summe = number + summe
        number= number-1
    print("Sum: ", summe)

def count_up(number):
    count = 0
    summe = 0
    while count <= number:
        print(count)
        summe = count + summe
        count = count+1
    print("Sum: ", summe)

def string_printer(string):
    print(string)
    ind = 0
    while ind < len(string):
        print(string[ind])
        ind = ind + 1
    

def reverse_string(string):
    print(string)
    ind = -1
    while ind >= -len(string):
        print(string[ind])
        ind = ind -1

def breaker():
    number = 0
    while True:
        guess = int(input(":"))
        if guess % 2 == 1:
            number += guess
        elif guess == 0:
            break
        elif guess % 2 == 0:
            continue
    print("sum =",number)

def print_range(ranger):
    num = len(ranger)
    ind = 0
    while num > ind:
        print(ranger[ind],end =" ")
        ind += 1

def print_range_for(ranger):
    for num in ranger:
        print(num,end=" ")

def for_reverses(string):
    final =""
    for st in string:
        final = st + final
    print(final)

def main():
    for_reverses("hello")
    print_range(range(1,10))
    print("")
    print_range_for(range(1,10))
    #breaker()
    #number = int(input("Enter Number: "))
    #countdown(number)
    #count_up(number)
    #string = input("Enter string: ")
    #string_printer(string)
    #reverse_string(string)


main()