"""
Students
Author: Ryan Robison
"""
import students

def main():
    stu = students.Student("123-abc","bob")
    stu.print_student()
    gcis = students.Course("GCIS-123",4,"A")
    gno = students.Course("idks",2,"B")
    gcis.print_course()
    gno.print_course()
    print(gcis.get_points())
    stu.add_course(gcis)
    stu.add_course(gno)
    stu.print_student()
    print(stu.get_gpa())

main()