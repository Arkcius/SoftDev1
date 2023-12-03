"""
Puropse of this code is to make multiple functions for to calculate area and volumes of shapes
Author: Ryan Robison
"""


#gets radius and calculates area of a circle and returns both
def circ_area():
    radius = float(input("Enter circle Radius: "))
    area = 3.14159*radius**2
    print("Circle: r =",radius,"area =",area)

#gets radius and calculates volume of a sphere and returns both
def sphere_vol():
    radius = float(input("Enter the spheres Radius: "))
    volume = 3.14159*(4/3)*radius**3
    print("Sphere: r =",radius,"volume =",volume)

#gets height and width of a rectangle and calculates and returns area
def rec_area():
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = height*width
    print("Rectangle: Height = ",height,", width = ",width,", area = ",area, sep="")

#gets side length and calculates area of a square and returns both
def sq_area():
    length = float(input("Enter square side length: "))
    area = length**2
    print("Square: side =",length,"area =",area)

#gets height and base of a isoceles triangle and returns area
def iso_area():
    base = float(input("Enter base length: "))
    height = float(input("Enter height length: "))
    area = (base*height)/2
    print("Isosceles triangle: Base = ",base,", height = ",height,", area = ",area, sep="")

#gets side length and calculates area of an equilateral triangle and returns it
def equ_area():
    side = float(input("Enter side length: "))
    area = 0.433*side**2
    print("Equilateral triangle: side =",side,"area =",area)

#gets base1 base2 and height of a trapezoid then calculates area and returns it
def trap_area():
    base1 = float(input("Enter base 1 length: "))
    base2 = float(input("Enter base 2 length: "))
    height = float(input("Enter height: "))
    area = ((base1+base2)/2)*height
    print("Trapezoid: Base 1 = ",base1,", base 2 = ",base2,", height = ",height,", area = ",area, sep="")

#main function calling all above functions
def main():
    circ_area()
    sphere_vol()
    rec_area()
    sq_area()
    iso_area()
    equ_area()
    trap_area()

#calling main
main()