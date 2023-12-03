"""
Purpose of the code is to make a landscape using turtle commands and shapes
Author: Ryan Robison
"""
import turtle
#function that takes in an x,y,height,width,pen,and fill color and draws and fills a rectangle at specified place
def Rec(x,y,height,width,pen,fill):
    turtle.up()
    turtle.goto(x,y)
    turtle.pencolor(pen)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()

#function takes in x,y,side length, then colors to make a triangle
def triangle(x,y,length,pen,fill):
    turtle.up()
    turtle.goto(x,y)
    turtle.pencolor(pen)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.down()
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.end_fill()

#takes in x y radius and colors to make a circle
def circle(x,y,radius,pen,fill):
    turtle.up()
    turtle.goto(x,y)
    turtle.pencolor(pen)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.down()
    turtle.circle(radius)
    turtle.end_fill()

#uses previous functions to make a tree 
def tree(x,y,width):
    turtle.up()
    Rec(x,y,width*1.5,width,"brown","brown")
    triangle(x-width,y+width*1.5,width*3,"green","green")
    triangle(x-width,y+width*2.5,width*3,"green","green")

#uses previous functions to make a tombstone
def tomb(x,y,width):
    turtle.up()
    Rec(x,y,width,width*3,"slategray","darkslategray")
    triangle(x,y+width*3,width,"slategray","darkslategray")
    triangle(x+width*2,y+width*3,width,"slategray","darkslategray")
    Rec(x+width/2,y+width*3,width*3/4,width*2,"darkslategray","darkslategray")
    Rec(x+width/2,y+width,width*2,width*2,"slategray","darkslategray")

#main function used to call others
def main():
    Rec(-500,-400,300,1000,"green","darkgreen")
    Rec(-500,-100,600,1000,"aqua","aqua")
    Rec(-500,-100,600,500,"midnightblue","midnightblue")
    Rec(-500,-400,300,500,"darkolivegreen","darkolivegreen")
    tree(260,-100,30)
    tree(80,-300,70)
    tomb(-300,-360,60)
    tomb(-120,-125,30)
    tomb(-450,-230,40)
    circle(350,200,100,"lemonchiffon","lightgoldenrodyellow")
    circle(-350,200,100,"white","ivory")
    circle(-300,250,100,"midnightblue","midnightblue")
    #adding an input so the program stops
    dones = input("Click enter to close: ")

main()