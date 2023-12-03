"""
Purpose to take in student grades and plot them
Author: Ryan Robison
"""
import plotter

# prompts user to enter y to quit and if they enter y or Y then returns true else return false
def terminate():
    returnal = input("Enter 'y' to quit:")
    if returnal.lower() == "y":
        print("Goodbye!")
        return True
    else:
        return False

#takes in file name first and last name and then if that student exists prints their grades
def plot_grades(filename,firstname,lastname):
    with open(filename) as file:
        #skips header line
        next(file)
        #for loop for all lines in file
        for line in file:
            #splits line then checkes if lastname and firstname match the student asked for
            liner = line.split(",")
            ind = 2
            if liner[ind-2] == lastname and liner[ind-1] == firstname:
                #if so makes title and initiates plot
                Title = firstname + lastname + " Grades"
                plotter.init(Title,"Grade","Score")
                #while loop to make the plot using datapoints
                while ind < 18:
                    try:
                        liners = float(liner[ind])
                    except ValueError:
                        liners = 0.0
                    plotter.add_data_point(liners)
                    ind +=1
                #plots and then goes to a new series
                plotter.plot()
                plotter.new_series()
                #return true that it worked
                return True
        #return false that it didnt
        return False

#takes in a split string and checks if its eligible and if it is trys to plotgrade it
def student_grades(string_line):
    try:
        #trys to run plotgrades on the stringline
        done = plot_grades(string_line[1],string_line[2],string_line[3])
        if done == True:
            print("Plot finished (window may be hidden)")
        elif done == False:
            print("Plot failed (no such student)")
    #if index error from not enough parameters prints usage
    except IndexError:
        print("Usage: stu <filename> <firstname> <lastname>")
    #if file not found prints no such file
    except FileNotFoundError:
        print("No such File:",string_line[1])

#main
def main():
    #while loop for while quitter equals false
    quitter = False
    while quitter == False:
        #asks for input then splits input at the spaces
        string = input(">>")
        string_split = string.split(" ")
        #if elif statment to check what was input
        #if nothing input prints enter command or quit
        if string == "":
            print("Enter a command or 'quit' to quit")
            #continue resets loop
            continue
        #if string_split[0] equals quit calls terminate function
        elif string_split[0] == "quit":
            quitter = terminate()
        #if string split 0 equals stu calles student grades with the whole string split
        elif string_split[0] == "stu":
            student_grades(string_split)
        # if string split 0 equals help prints help message
        elif string_split[0] == "help":
            print("stu <filename> <first name> <last name> - plot student grades item\nquit - quits\nhelp - displays this message")



main()