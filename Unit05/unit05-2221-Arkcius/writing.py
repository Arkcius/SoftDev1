""" 
Purpose to write and plot a students set of grades
Author: Ryan Robison
"""

import csv
import re
import plotter


#purpose to take in file and first and last name and look through csv and if student found print their grades
def plot_grades(infile, firstname, lastname):
    #opens file
    with open(infile) as filename:
        #makes file a cvs reader of filename
        file = csv.reader(filename)
        #skips to next line
        next(file)
        #for loop for all lines in file
        for line in file:
            ind = 3
            #checks if both firstname and lastname are found in section 0 of line which is the name section
            if re.findall(firstname,line[0]) and re.findall(lastname,line[0]):
                #if so makes a title and initiates plot
                Title = firstname + lastname + " Grades"
                plotter.init(Title,"Grade","Score")
                #while loop for all 30 grade points
                while ind < 30:
                    #converts line section for each grade into a float and adds it to data points
                    liners = float(line[ind])
                    plotter.add_data_point(liners)
                    ind +=1
                #plots datapoints and makes a new series
                plotter.plot()
                plotter.new_series()

#takes in file and lastname of student and if it finds them in the file prints it out and writes to outrow file of students data
def put_grades(infile,outfile,lastname):
    #opens file
    with open(infile) as filename:
        #makes file a csv reader
        file = csv.reader(filename)
        #skips to next line
        next(file)
        #initiates fout for out file and the writer
        fout = open(outfile,"w",newline="")
        writer = csv.writer(fout, quoting=csv.QUOTE_MINIMAL)
        #scans the file for last name in line[0] which is the name section
        for line in file:
            if re.findall(lastname,line[0]):
                #if found writes the line in the file and prints the line
                print(line)
                writer.writerow(line)

#function takes in filename and last name and returns grade average
def get_average(filename,lastname):
    #opens file
    with open(filename) as files:
        #makes file csv.reader and skips header line
        file = csv.reader(files)
        next(file)
        #checks every line in file
        for line in file:
            #if finds the last name in line[0] the name section
            if re.findall(lastname,line[0]):
                #makes ind start at 3 and makes count and total = 0
                ind = 3
                total = 0
                count = 0
                #then while ind < 30
                while ind < 30:
                    #trys to at to float of line[ind] to total and adds 1 to count but if fails then adds 0 to both
                    try:
                        total += float(line[ind])
                        count += 1
                    except:
                        count += 0
                        total += 0
                    ind += 1
                #calculates and returns average
                avg = total/count
                return avg



#main
def main():

    studentA = get_average("data/full_grades_100.csv","Zagar")
    print("Student Name: Zagar, Leon\tGrade Average(mean): ",studentA )
    studentb = get_average("data/full_grades_100.csv","Gommer")
    print("Student Name: Gommer, Blake\tGrade Average(mean): ",studentb )



    """ Tests for the other functions
    print(get_average("data/full_grades_100.csv","Gommer"))
    put_grades("data/full_grades_999.csv","out_rows.txt","Gwilt")
    plot_grades("data/full_grades_010.csv",'Sion','Lobasso')
    end = input("Enter to end: ")
    """

main()