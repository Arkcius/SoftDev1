"""
Review part 2 electric boogaloo
Author:Ryan Robison
"""
import csv
import random
import node_stack
import node

def street_type(filename):
    with open(filename) as filer:
        file = csv.reader(filer)
        streets = dict()
        next(file)
        for line in file:
            try:
                streets[line[1]] += 1
            except:
                streets[line[1]] = 1
        return streets

def search(filename,street):
    with open(filename) as filer:
        file = csv.reader(filer)
        streets = set()
        for line in file:
            if line[0].upper() == street.upper():
                streets.add(line[1])
        if len(streets) == 0:
            return None
        return streets

def check(filename,street,type):
    with open(filename) as filer:
        file = csv.reader(filer)
        next(file)
        found = False
        for line in file:
            if line[0] == street.upper():
                if line[1] == type.upper():
                    print("Found ",street," ",type)
                    found = True
        if found == False:
            print("Not Found")

class Exam:
    __slots__ = ["__student","__pointsmax","__pointsearned"]

    def __init__(self,student,max):
        self.__student = student
        self.__pointsmax = max
        self.__pointsearned = 0

    def get_student(self):
        return self.__student
    def get_max(self):
        return self.__pointsmax
    def get_earn(self):
        return self.__pointsearned
    def set_earn(self,value):
        self.__pointsearned = value

    def return_grade(self):
        out = (self.__pointsearned/self.__pointsmax) * 100
        return out

    def __str__(self):
        out = (self.__student + " ("+str(self.return_grade())+")")
        return out

    def __eq__(self,other):
        if type(self) == type(other):
            return self.get_student() == other.get_student()
        else:
            return False
    def __lt__(self,other):
        if type(self) == type(other):
            if self.get_student() != other.get_student():
                return self.return_grade() > other.return_grade()
            else:
                return self.get_student() == other.get_student()
    def __hash__(self):
        return hash(self.return_grade())*1000 + len(self.get_student())


    
def admin(students):
    stacker = node_stack.Stack()
    for elements in students:
        print("Completed: ",elements)
        stacker.push(elements)
    return stacker

def grade(stacker):
    listo = []
    while stacker.size()>0:
        student = stacker.pop()
        student.set_earn(random.randint(0,int(student.get_max())))
        print("Graded: ",student)
        listo.append(student)
    return listo

def enter(listo):
    for elements in listo:
        print("Entered: ",elements)

def sorter(listo):
    listo.sort()
    for elements in listo:
        print(elements)


def main():
    streets = street_type("data/streets.csv")
    print("DR Amount: ", streets["DR"])
    check("data/streets.csv","RED LEAF","CT")
    vista = search("data/streets.csv","VISTA") 
    print(vista)
    st1 = Exam("Bob",50)
    st2 = Exam("Joe",50)
    st3 = Exam("Sarah",50)
    st4 = Exam("Jay",50)
    st5 = Exam("Leo",50)
    st = [st1,st2,st3,st4,st5]
    print("Admin")
    stacker = admin(st)
    print("\nGraded")
    listo = grade(stacker)
    print("\nEnter")
    enter(listo)
    print("\nSorted")
    sorter(listo)

main()