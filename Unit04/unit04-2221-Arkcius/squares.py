"""
Purpose to draw squares
Author: Ryan Robison
"""
import turtle
import math

#made a square fucntion that draws a square with given length and color
def squares(length,color):
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()

#function to take in previous squares length and using pthag
#returns the new squares length
def pthag(length):
    return math.sqrt((length/2)**2+(length/2)**2)

#draw squares func that draws 6 concentric squares at 45 degrees from last
def draw_squares(length):
    turtle.up()
    #first square with goto and length
    turtle.goto(-length/2,-length/2)
    squares(length,"red")
    #second square starts at same x value but at y=0
    turtle.goto(-length/2,0)
    #turn -45 and then make length2 using pthag
    turtle.setheading(-45)
    length2 = pthag(length)
    squares(length2,"blue")
    #make length3 using pthag
    length3= pthag(length2)
    #having turtle go to its bottom left corner and setting heading
    turtle.goto(-length3/2,-length3/2)
    turtle.setheading(0)
    squares(length3,"yellow")
    #has turtle goto middle middle of the left side of square 3 and turn 45 for next
    turtle.goto(-length3/2,0)
    turtle.setheading(-45)
    #makes sidelength for square 4 and then makes square 4
    length4 =pthag(length3)
    squares(length4,"green")
    #makes side length for square 5 then goto bottom left of square 5
    length5= pthag(length4)
    turtle.goto(-length5/2,-length5/2)
    #set heading then draw square 5
    turtle.setheading(0)
    squares(length5,"orange")
    #makes turtle go to starting point for square 6 and make its length
    turtle.goto(-length5/2,0)
    turtle.setheading(-45)
    length6 =pthag(length5)
    #make square 6 and return its length
    squares(length6,"pink")
    return length6



#main that calls draw squares and prints then length of square 6
def main():
    small_length = draw_squares(400)
    print("Small length size: ", small_length)
    end = input("Enter to end: ")

main()