"""
Purpose to test array activites
Author: Ryan Robison
"""

import arrays
import random
import turtle

random.seed(1)

def making_arrays():
    noproto = arrays.Array(5)
    print(noproto)
    protozero = arrays.Array(1,0)
    print(protozero)
    empty = arrays.Array(10,"")
    print(empty)
    falsea = arrays.Array(20,False)
    print(falsea)

def while_fill(an_array):
    index = 0
    length = len(an_array)
    while index < length:
        an_array[index]=index
        index+=1

def for_fill(an_array):
    index=0
    length = len(an_array)
    for index in range(length):
        an_array[index]=index

def roll_the_die(sides):
    return random.randint(1,sides)

def countdown(n):
    if n == 0:
        print(n)
        return 0
    else:
        print(n, end=" ")
        return n + countdown(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def circles(radius,depth):
    if depth == 0:
        return 0
    elif depth == 1:
        turtle.circle(radius)
        return 3.14*radius*2
    else:
        total = 3.14*radius*2
        for _ in range(4):
            turtle.circle(radius,90)
            total += circles(radius/2,depth-1)
        circles(radius/2,depth-1)
        return total

def count_up(number):
    if number == 0:
        print(number)
    else:
        count_up(number-1)
        print(number)

def main():
    array_a = arrays.Array(10)
    print(array_a)
    while_fill(array_a)
    print(array_a)
    for_fill(array_a)
    print(array_a)
    making_arrays()
    for i in range(10):
        number = roll_the_die(6)
        print("Rolling a 6-sided die: ", number)
    print(countdown(5))
    print(factorial(10))
    print(circles(200,3))
    count_up(10)

main()
    