"""
Purpose to make a pixel art of using a draw rows function with colors
Author: Ryan Robison
"""
import turtle
import pixart

#gets a String of colors and a starting index and returns the color
def get_color(ColorString,index):
    #makes an empty string
    color = ""
    #while loop for while both the current index doesnt equal a comma and while it is not at the max length
    while  index != len(ColorString) and ColorString[index] != ",":
        #adds the colorstring index to the color string
        color = color + ColorString[index]
        #increase index by 1
        index += 1
    #returns color
    return color

#draws a row when given a string of colors
def draw_row(Colors):
    #sets index to 0 and columns to 0
    index = 0
    col = 0
    #while index is less than the length of colors and col is less than max collumns
    while index <= len(Colors) and col < pixart.COLUMNS:
        #color equals get color of the string and current index
        color = get_color(Colors,index)
        #draws a pixel of the gotten color
        pixart.pix(color)
        # increases index by length of color plus one to account for comma
        index += len(color)+1
        #adds 1 to col variable
        col += 1

#prompts user to input color lines and then continus prompting till all rows filled
def block():
    #row = 0 to start
    row = 0
    #while loop for while the row is less than the max rows
    while row < pixart.ROWS:
        #prompt user for input of the color line
        ColorString = input("Enter Color Line: ")
        #draws row with the color line
        draw_row(ColorString)
        #adds one to the row
        row += 1
        #moves the cursor down one row
        pixart.move(0,row)

def main():
    pixart.initialize()
    block()
    end = input("Enter to end:")

main()