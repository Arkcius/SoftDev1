"""
Puropse to test turtlecraft.py
Author: Ryan Robison
"""

import turtlecraft

#testing get color for one color
def test_get_color():
    expect = "blue"
    color = turtlecraft.get_color("blue",0)
    assert (color == expect)

#testing get color for getting two colors
def test_get_color2():
    expect = "blue"
    expect2 = "green"
    color1 = turtlecraft.get_color("red,blue,green",4)
    color2 = turtlecraft.get_color("red,blue,green",9)
    assert(color1==expect and color2 == expect2)

