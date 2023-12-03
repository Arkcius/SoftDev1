"""
Purpose to start with classes
Author: Ryan Robison
"""

class Student:
    __slots__ = ['id', 'name', 'credits', 'gpa']

    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.credits = 0
        self.gpa = 0.0
    

def print_student(student):
    print("Student: ",student.id,student.name,
    student.credits,student.gpa)

def main():
    student1 = Student("123-ABC","Cyrus")
    student2 = Student("234-BNM", "Rex")
    student1.credits = 24
    student1.gpa = 2.7
    print_student(student1)
    print_student(student2)


main()