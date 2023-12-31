"""
A Student class.

@author GCCIS Faculty
"""

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

QUALITY_POINTS = {
    GRADES[0]: 4.0,
    GRADES[1]: 3.67,
    GRADES[2]: 3.33,
    GRADES[3]: 3.0,
    GRADES[4]: 2.67,
    GRADES[5]: 2.33,
    GRADES[6]: 2.0,
    GRADES[7]: 1.67,
    GRADES[8]: 1.0,
    GRADES[9]: 0,
    GRADES[10]: 0 # no grade
}

class Student:
    """
    A class that represents a student with fields for ID, name, credits, and
    GPA.
    """
    __slots__ = ["__id", "__name", "__credits", "__gpa","__courses"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0
        self.__courses = []
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def get_gpa(self):
        qp = 0
        tc = 0
        for course in self.__courses:
            tc += course.get_credits()
            qp += course.get_points()
        if tc == 0:
            return 0
        else:
            return qp/tc
    def set_gpa(self,gpa):
        self.__gpa = gpa
    def set_credits(self,credits):
        self.__credits = credits
    def add_course(self,course):
        self.__courses += [course]
        self.__credits += course.get_credits()

    def print_student(self):    
        print("Student ID: ", self.__id, " name: ", self.__name, 
        " credits: ", self.__credits, " GPA: ", self.__gpa, sep="")

class Course:
    __slots__ = ["__name","__credits","__grade"]
    def __init__(self,name,credits,grade):
        self.__name = name 
        self.__credits = credits
        self.__grade = grade
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def get_grade(self):
        return self.__grade
    def set_grade(self,grade):
        self.__grade = grade
    def get_points(self):
        cred = QUALITY_POINTS[self.__grade]
        return cred*self.__credits

    def print_course(self):
        print("Course Name: ",self.__name," Credits: ",self.__credits," Grade: ",self.__grade)
