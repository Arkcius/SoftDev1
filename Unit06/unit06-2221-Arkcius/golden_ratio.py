"""
Purpose to use the golden ratio
Author: Ryan Robison
"""

import arrays
import turtle

#function returns the fibonaci number for given index
def fibonacci(number):
    #if number is less than or equal to zero returns undefined
    if number <= 0:
        return "undefined"
    #if number is 1 or 2 returns 0 or 1 respectively
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    #all other cases call return the the fibonacci of number -1 plus fibonacci of number -2 using recursion to recall the function
    else:
        return (fibonacci(number-2)+fibonacci(number-1))

#fills an array with the fibonacci numbers up to arrays length
def fill_fibonacci_array(array,index = 0):
    #sets the index of array to the fibonacci of the index plus 1 cause fibonacci zero is undefined
    array[index] = fibonacci(index+1)
    #if the index is less than array length -1 then it calls recursion for the next index
    if index < len(array)-1:
        fill_fibonacci_array(array,index+1)
    #returns array
    return array

#prints the ratios of two adjacent fibonacci numbers for a whole array
def print_ratios(array, index = 0):
    #sets a and b to array index and array index+1
    a = array[index]
    b = array[index+1]
    #if the array[index] == 0 then ba and abb are set to undefined and nothing
    if array[index] == 0:
        ba = "undefined"
        abb = ""
        #prints modified version for undefined
        print(f"{a:>4n} {b:>4n}  {ba}")
    else:
        #otherwise ba is b/a and abb is a+b/b then prints this line
        ba = b/a
        abb = (a+b)/b
        print(f"{a:>4n} {b:>4n}  {ba:.5f}  {abb:.5f}")
    #if the index is 2 less than the array length, so that we dont get the last number and a blank, then calls recursion of the function with index+1
    if index < len(array)-2:
        print_ratios(array,index+1)

#draws fibonaci sprial for an preset array length of 13
def draw_fibonaci_spiral():
    #makes the array and fills it with the fibonachi numbers
    aray = arrays.Array(15)
    aray = fill_fibonacci_array(aray)
    #makes length for the array for the index
    length = len(aray)-1
    #moves the turtle left by the biggest fibonachi to more center it then sets heading to start drawing
    turtle.up
    turtle.setheading(180)
    turtle.forward(aray[length])
    turtle.setheading(90)
    #calls draw spiral
    draw_spiral(aray,length)
    
#draws the spiral of the given array and index    
def draw_spiral(aray,index):
    #sets turtle down
    turtle.down()
    #makes turtle go in a box for length aray[index]
    for _ in range(4):
        turtle.forward(aray[index])
        turtle.right(90)
    #turns turtle and draws the arc then turns turtle back
    turtle.left(180)
    turtle.circle(aray[index],-90)
    turtle.left(180)
    #if the index is greater than 0 it keeps going
    if index > 0:
        draw_spiral(aray,index-1)

#main
def main():
    aray = arrays.Array(20)
    aray = fill_fibonacci_array(aray)
    print(aray)
    print_ratios(aray)
    draw_fibonaci_spiral()
    end = input("enter to close: ")

main()