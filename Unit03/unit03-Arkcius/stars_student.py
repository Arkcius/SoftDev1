"""
Draws a sky filled with stars and planets.

@author
"""

import random
import turtle

def tweak(speed, tracer):
    """
    Adjust the turtle's speed and tracer settings so that it can be sped up
    or slowed down as needed for visual debugging.
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def random_yellow():
    """
    Sets the turtle's fill color to a random shade of yellow using RGB values.
    """
    # the random.random() function returns a floating point value between
    # 0.1 and 1.0. This expression guarantees that the red value will be
    # between 0.5 and 1.0.
    red = 0.5 + random.random() * 0.5
    green = red
    blue = red / 2

    # the turtle color can be set using RGB values ranging from 0.0 to 1.0. In
    #  this case the red and green values are between 0.5 and 1.0 and the blue
    # value is half the value - this guarantees a shade of yellow.
    turtle.color(red, green, blue)
    """
    semantic error
    blue and green parameters flipped resulting in pink fill
    switch blue and green
    """
    turtle.fillcolor(red, green, blue)

def random_move():
    """
    Moves the turtle to a random location and orientation on the screen.
    """
    #changed broder to be smaller
    border = 800
    x = random.randint(-border, border)
    """
    Syntax error
    Missing "," after first number
    added the comma after the first number
    """
    y = random.randint(-border, border)
    """
    semantic error
    turtle.goto is not using the y
    add the y
    """
    turtle.goto(x, y) 

    angle = random.randint(0, 360)
    """
    semantic error
    stars werent changing their angle 
    added turtle.setheading(angle so when they moved the turtle also stared facing a random way)
    """
    turtle.setheading(angle)

"""
Syntax
missing ":" after function
Add : to the end of the function
"""
def star_line(length):
    turtle.forward(length)
    turtle.right(144)
    turtle.forward(length)
    turtle.left(72)

def draw_star(length):
    """
    Draws a star at the turtle's current location and orientation.
    """
    random_yellow()

    turtle.down()
    turtle.begin_fill()

    """
    semantic error
    had to change all of the turtle.(right or left) and changed the values to make them make the star
    swapped the turtle.right and turtle.left as well and made their values 144 and 72 respectivly
    """
    star_line(length)
    star_line(length)
    star_line(length)
    star_line(length)
    star_line(length)
    turtle.end_fill()    

#moves the turtle up and then randomly positions and orientates it then calls draw star for a random int between 5 and 10
def random_star():
    turtle.up()
    random_move()
    #gets a random int between 5 and 10
    length = random.randint(5,10)
    draw_star(length)

#takes in xy radius and fill color and then draws world starting at the bottom of the coordinates with that radius and fill
def draw_world(x,y,radius,fill):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pencolor(fill)
    turtle.fillcolor(fill)
    turtle.begin_fill()
    turtle.down()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()

#draws 100 random stars and then 3 worlds
def draw_celestial_bodies():
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    random_star()
    draw_world(100,20,150,"red")
    draw_world(-300,-10,40,"white")
    draw_world(-100,200,100,"blue")

def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    turtle.bgcolor("black")
    """
    runtime error
    func tweak needs the speed to be first followed by the tracer
    switched the true and 1
    """
    #also made it 100 to make it go faster
    tweak(100, True)
    """
    runtime error
    input needs to be an int or float to work for func draw star
    added the int() around the input
    """
    #length = int(input("Enter length of star to draw (e.g. 100): "))
    #draw_star(length)
    draw_celestial_bodies()
    """
    runtime error
    func tweak needs the speed to be first followed by the tracer
    switched the true and 1
    """
    tweak(1, True)
    """
    semantic error
    turtle.hide() not a thing
    made it turtle.hideturtle()
    """
    turtle.hideturtle()
    """
    semantic error
    input needed to be into a variable
    added an end variable before input
    """
    end = input("Press enter to continue... ")

main()