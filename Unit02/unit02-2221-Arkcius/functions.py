"""
Purpose of this program is to do the homework which asks for multiple functions and also teaches about sep and end
Author: Ryan Robison
"""
#function to gather current and birth month and year and calculate a persons age in months
def age_calc():
    cyear = int(input("Input current year: "))
    cmonth = int(input("Input current month as a number: "))
    byear = int(input("Input birth year: "))
    bmonth = int(input("Input birth month: "))
    #now that inputs are done it calculates how many months and prints
    year = cyear-byear
    month = cmonth-bmonth
    age = year*12+month
    print("Your age in months:",age)

#main function to call other functions
def main():
    age_calc()

#calling main
main()