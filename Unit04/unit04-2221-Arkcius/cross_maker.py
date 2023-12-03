"""
Purpose to make a program that will take in strings and place them either horizontal or vertical in boxes like scrabble
Author: Ryan Robison
"""
import turtle

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20

#function to move the cursor to the top left of the pixel block
def move(col,row):
    turtle.up()
    x = col*PIXEL_SIZE+(-COLUMNS/2*PIXEL_SIZE)
    y = (-row)*PIXEL_SIZE+(ROWS/2*PIXEL_SIZE)
    turtle.goto(x,y)

#creates the letter in a box draw at said pixel location
def letter(String):
   box()
   turtle.up()
   turtle.right(90)
   turtle.forward(PIXEL_SIZE)
   turtle.left(90)
   turtle.forward(PIXEL_SIZE/2)
   turtle.write(String, align='center', font = ("Arial",19,"normal"))
   turtle.left(180)
   turtle.forward(PIXEL_SIZE/2)
   turtle.right(90)
   turtle.forward(PIXEL_SIZE)
   turtle.right(90)

#draws a box with a color
def box():
    turtle.fillcolor("lavender")
    turtle.begin_fill()
    turtle.down()
    for _ in range(4):
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()
    
#check to see if input word is valid and will fit in area
def valid(x,y,word,is_horizontal):
    if is_horizontal == True:
        if 0<=y<=19 and 0<=x<=19-len(word):
            return True
        else:
            return False
    if is_horizontal == False:
        if 0<=y<=19-len(word) and 0<=x<=19:
            return True
        else:
            return False

#function takes in string and converts it to needed variables and prints
def write(string):
    #making empty variables and 0 index
    ind = 0
    x=""
    y=""
    st=""
    HvV=""
    #while loop for while the index isnt a space and sets x to everything before
    while string[ind]!=" ":
        x = x+string[ind]
        ind+=1
    #makes x an integer and increases ind past the space
    x = int(x)
    ind+=1
    
    #functions exactly the same as the x above just for the y and second number
    while string[ind]!=" ":
        y = y + string[ind]
        ind += 1
    y = int(y)
    ind+=1
    
    #while loop to add the letters of the string too the st variable and increase ind by 1 each time and stops when string[ind] equals a space
    while string[ind]!=" ":
        st = st + string[ind]
        ind+=1
    
    #checks if last letter in string is an h or v for wheter vertical or horizontal
    if string[len(string)-1] == "h":
        HvV = True
    elif string[len(string)-1] == "v":
        HvV = False
    
    #if the command is valid it proceeds
    if valid(x,y,st,HvV) == True:
        move(x,y)
        #if horizontal prints and moves forward if vertical prints and moves down
        if HvV == True:
            for index in range(len(st)):
                letter(st[index])
                move(x+index+1,y)
        elif HvV == False:
            for index in range(len(st)):
                letter(st[index])
                move(x,y+index+1)        
    #if not valid prints error
    elif valid(x,y,st,HvV) == False:
        print("Error command not valid")

def main():
    move(0,0)
    string = " "
    while string != "":
        string = input("Enter command or enter nothing to close:")
        write(string)


main()