import math

class Circle:
    __slots__ = ['__center', '__radius']

    #just initializes with given variables
    def __init__(self,center,radius):
        self.__center = center
        self.__radius = radius

    #checks if they intersect and if they do return true
    def intersect(self,other):
        if type(self) == type(other):
            #gets the radius sum and distance between two centers
            rad = self.__radius + other.__radius
            dis = math.sqrt((self.__center[0]-other.__center[0])**2+\
                (self.__center[1]-other.__center[1])**2)
            #if radius sum is bigger than distance then they intersect
            return rad > dis
        else:
            return False
    #less than for sorting based off their radius so smaller radius is smaller
    def __lt__(self,other):
        if type(self) == type(other):
            return self.__radius < other.__radius
        return False
        
    #repr for when being printed that shows center and radius
    def __repr__(self):
        return "Center: (" + str(self.__center[0])+", "+str(self.__center[0])\
            +") radius: "+ str(self.__radius)
    
#main
def main():
    circle1 = Circle((0, 0), 2)
    circle2 = Circle((4, 0), 3) 
    circle3 = Circle((3, 3), 1)
    a_list = [circle1, circle2, circle3]
    a_list.sort()
    print(a_list)
    print("circle1 and circle2 intersect:", circle1.intersect(circle2)) # True
    print("circle1 and circle3 intersect:", circle1.intersect(circle3)) # False
    print("circle2 and circle3 intersect:", circle2.intersect(circle3)) # True

main()           
    
