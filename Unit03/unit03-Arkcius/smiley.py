"""
Makeing a smiely face
Author: Ryan Robison
"""
import turtle

#function takes in coordinates radius and color and draws a circle
def draw_circle(x,y,radius,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.pencolor("black")
    turtle.fillcolor(color)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()


#takes in center x and y and radius and color and makes circle
def draw_center_circle(x,y,radius,color):
    #raise the pen
    turtle.up()
    # go to center
    turtle.goto(x,y)
    #set pen color and fill color
    turtle.pencolor("black")
    turtle.fillcolor(color)
    #move forward radius
    turtle.forward(radius)
    #turn left 90
    turtle.left(90)
    #pen down
    turtle.down()
    #begin fill
    turtle.begin_fill()
    #draw circle
    turtle.circle(radius)
    #end fill
    turtle.end_fill()
    #pen up
    turtle.up()
    #turn left 90
    turtle.left(90)
    #forward radius
    turtle.forward(radius)
    #turn left 180 to resest orientation
    turtle.left(180)

def tweak(speed,tracer):
    turtle.speed(speed)
    turtle.tracer(tracer)

#takes in x,y colors and head radius to draw smiley head
def draw_smiley(x,y,radius,hcolor,ncolor,icolor,mcolor):
    #draws head with its color then nose at 1/10th the size with its own color
    draw_center_circle(x,y,radius,hcolor)
    radius_tenth = radius/10
    radius_third = radius/3
    x_offset = radius*.35
    y_offset = radius*.25
    draw_center_circle(x,y,radius_tenth,ncolor)
    draw_eye(x+x_offset,y+y_offset,radius_third,icolor)
    draw_eye(x-x_offset,y+y_offset,radius_third,icolor)
    draw_mouth(x,y-2*radius_tenth,2*radius_third,mcolor)

#takes in x,y,radius and iris color and creates an eye of concentric circles
def draw_eye(x,y,radius,color):
    draw_center_circle(x,y,radius,"white")
    draw_center_circle(x,y,radius/2,color)
    draw_center_circle(x,y,radius/4,"black")

#takes x,y,radius and fill color and makes a semicircle mouth
def draw_mouth(x,y,radius,fill):
    #making turtle be up and setting colors
    turtle.up()
    turtle.goto(x,y)
    turtle.pencolor("black")
    turtle.fillcolor(fill)
    #moving to outer edge and setting down turtle
    turtle.left(180)
    turtle.forward(radius)
    turtle.begin_fill()
    turtle.down()
    #making semicircle with the radius
    turtle.left(90)
    turtle.circle(radius,180)
    #end fill and move turtle up
    turtle.end_fill()
    turtle.up()
    #sending back to origin
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(180)


def main():
    tweak(10,False)
    draw_smiley(-100,-20,100,"slategray","lightgray","purple","black")
    draw_smiley(200,130,200,"slategray","lightgray","purple","black")
    end = input("Enter to end: ")

main()