"""
REVIEW
AUTHOR: Ryan Robiosn
"""
"""
look over old power points 
and sleep well night before
"""
import csv
import arrays


def starts_with(filename,letter):
    with open(filename) as file:
        count = 0
        for line in file:
            liner = line.lower().split()
            for word in liner:
                if word[0] == letter.lower():
                    count+= 1
        return count

def zip_lookup(filename,zipcode):
    with open(filename) as filer:
        file = csv.reader(filer)
        for line in file:
            if line[0] == zipcode:
                return line
        raise ValueError ("Zip Not Found")

def ispower(a,b):
    if a == 1:
        return True
    elif a%b==0:
        return ispower(a/b,b)
    else:
        return False

def what_power(a,b,x=0):
    if a == 1:
        return x
    elif a%b == 0:
        return what_power(a/b,b,x+1)
    else:
        raise ValueError("A is not power of B")

def fill_array(anarry,start=0,step=1,index=0):
    if index >= len(anarry):
        return
    else:
        anarry[index] = start
        fill_array(anarry,start+step,step,index+1)
def arrays_equal(array1,array2,index = 0):
    if index == len(array1):
        return index == len(array2)
    elif index == len(array2):
        return False
    elif array1[index] == array2[index]:
        return arrays_equal(array1,array2,index+1)
    else:
        return False

def main():
    for ascii in range(97,123):
        letter = chr(ascii)
        print(letter, ":",starts_with("data/atotc.txt",letter))
    inputer = "1"
    filename = "data/zip_codes.csv"
    while inputer != "":
        inputer = input("Enter Zip to find: ")
        if inputer == "":
            print("Bye")
            break
        try:
            zipp = zip_lookup(filename,inputer)
            print(zipp)
        except ValueError:
            print("Invalid zip: ",inputer)
        except FileNotFoundError:
            print("File wrong")
            inputer = ""
    print(ispower(25,5))
    print(ispower(27,2))
    print(what_power(125,5))
    tester = arrays.Array(10)
    tester2 = arrays.Array(10)
    tester3 = arrays.Array(10)
    fill_array(tester,3,2)
    fill_array(tester2,3,2)
    fill_array(tester3,3,1)
    print(tester)
    print(arrays_equal(tester,tester2))
    print(arrays_equal(tester,tester3))
main()