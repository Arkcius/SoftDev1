"""
Purpose to make pixel art
Author:Ryan Robison
"""
import turtle

PIXEL_SIZE = 30
ROWS = 16
COLUMNS = 16

def initialize():
    turtle.reset()
    turtle.speed(0)
    turtle.up()
    turtle.goto(-COLUMNS/2*PIXEL_SIZE,ROWS/2*PIXEL_SIZE)
    turtle.pencolor("black")
    turtle.fillcolor("white")
    
def pix(color):
    side = 0
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.down
    while side < 4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        side = side +1
    turtle.end_fill()
    turtle.up()
    turtle.forward(PIXEL_SIZE)

def move(col,row):
    turtle.up()
    x = col*PIXEL_SIZE+(-COLUMNS/2*PIXEL_SIZE)
    y = (-row)*PIXEL_SIZE+(ROWS/2*PIXEL_SIZE)
    turtle.goto(x,y)
    
def draw_row(col,row,number,color = "red"):
    turtle.up()
    move(col,row)
    for _ in range(number):
        pix(color)

def draw_square(col,row,size,color="green"):
    turtle.up()
    move(col,row)
    rowss = 0
    for rowss in range(size):
        move(col,row+rowss)
        for _ in range(size):
            pix(color)

def draw_rectangle(col,row,width,height,color="orange"):
    turtle.up()
    h=0
    for h in range(height):
        move(col,row+h)
        for _ in range(width):
            pix(color) 

def main():
    initialize()
    draw_rectangle(0,0,2,3)
    draw_square(1,1,3)
    draw_row(3,4,5)
    pix("purple")
    move(2,1)
    pix("red")
    end = input("Enter to close: ")

main()
    