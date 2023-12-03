"""
Mini_Practicum 2
Author: Ryan Robison
"""
import turtle
#takes in height in inches and gives back in feet and inches
def convert_height():
    height = int(input("Enter height in inches: "))
    feet = int(height/12)
    #uses mod to get the remainder
    inch = height % 12
    print("You are ",feet,"' ",inch,'" ',"tall", sep="")


#makes the background
def back():
    #goes to a far away point then makes a large square
    #and fills it with cyan
    turtle.up()
    turtle.goto(-800,-600)
    turtle.fillcolor("cyan")
    turtle.begin_fill()
    turtle.down()
    #square drawing
    turtle.forward(1600)
    turtle.left(90)
    turtle.forward(1600)
    turtle.left(90)
    turtle.forward(1600)
    turtle.left(90)
    turtle.forward(1600)
    turtle.left(90)
    turtle.end_fill()

#takes in x,y, and radius and builds a snowman
def snow_man(x,y,radius):
    #calls back function to make background
    back()
    #goes to starting point and sets fill to white
    turtle.up()
    turtle.goto(x,y)
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.down()
    #drawing the three circles
    turtle.circle(radius)
    turtle.up()
    turtle.goto(x,y+radius*2)
    turtle.down()
    turtle.circle(radius*.75)
    turtle.up()
    turtle.goto(x,y+radius*3.5)
    turtle.down()
    turtle.circle(radius/2)
    turtle.end_fill()
    #input to stop turtle from closing when finished
    end = input("Enter when done to close: ")





def main():
    #main to call both functions
    convert_height()
    snow_man(0,-100,100)

main()
