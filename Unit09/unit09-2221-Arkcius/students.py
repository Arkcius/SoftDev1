"""
Purpose to make student sets
Author: Ryan Robison
"""

def make_student(id,name):
    return[id,name,0,0.0]

def add_student(popu,id,name):
    for index in range(len(popu)):
        student = popu[index]
        if student[0] == id:
            popu.pop(index)
            break
    new_student = make_student(id,name)
    popu += [new_student]

def get_student(popu,id):
    for student in popu:
        if student[0]==id:
            return student
    return None

def add_credits(pop,id,credits):
    student = get_student(pop,id)
    if student is not None:
        student[2] += credits

def get_credit(popu,id):
    student = get_student(popu,id)
    if student is not None:
        return student[2]
    return None

def main():
    a = make_student(123,"Abek")
    print(a)
    pop = []
    add_student(pop,"cb1234","Charlie Brown")
    add_student(pop,"sb4567","Sally Brown")
    add_student(pop,"kh4444","Kak Hare")
    add_student(pop,"cm8392","Cyrus Morn")
    print(pop)
    sd = get_student(pop,"cm8392")
    sc = get_student(pop,"kk3221")
    print(sd,sc)
    add_credits(pop,"cm8392",6)
    print(get_credit(pop,"cm8392"))

main()