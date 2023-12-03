"""
Purpose of the program is to test and play around with turtle
Author: Ryan Robison
"""
import turtle

def test_drive():
    turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)

def square(side):
    turtle.down()
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)

def turtle_state():
    down = turtle.isdown()
    head = turtle.heading()
    turtlex = int(turtle.xcor())
    turtley = int(turtle.ycor())
    print("Is turtle down,",down)
    print("Turtle heading: ",head)
    print("Turtle coordinate(x,y)",turtlex,",",turtley )

def main():
    turtle_state()
    test_drive()
    square(100)
    square(200)
    turtle.up()
    turtle.forward(100)
    square(300)
    turtle_state()

main()
Stopper = input("Enter to close: ")