"""
Usinging return and making functions that do operations
Author: ryan robison
"""
#Value of PI for first 5 decimals
PI = 3.14159

#below four functions take in two numbers x,y and then does the basic operations to them
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def circumference(radius):
    return 2*PI*radius

def area(radius):
    return PI*radius**2

#main prompting for input that is turned into an in and then
#prints add subtracy multiply and divide of x and y
def main():
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))
    rad = int(input("Enter radius: "))
    print(circumference(rad))
    print(area(rad))

main()