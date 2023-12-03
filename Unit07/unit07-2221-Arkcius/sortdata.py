"""
Purpose to sort data
Author: Ryan Robison
"""
import arrays
import csv

#function that takes in file colum and size and returns an array of the data sorted from that collum
def sort_col(filepath,i_col,size):
    try:
        #try except for if file found or not
        with open(filepath) as filename:
            #opens file and makes it a csv reader and skips first line
            file = csv.reader(filename)
            next(file)
            #makes an array to the size given
            list = arrays.Array(size)
            #sets index to 0
            index = 0
            #for lines in file it trys to set list to that lines collum if able to be made an int and returns invalid if it cant
            for line in file:
                try:
                    list[index] = int(line[i_col])
                except ValueError:
                    print("Invalid Value")
                #increase index
                index+=1
            #insertion sort the list
            insertion_sort(list)
            #reutnr list
            print(list)
    except FileNotFoundError:
        print("File not found")
    
#takes in array and 2 indexes and swaps them in the array
def swap(array,a,b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

#chekcks if the index to the left is bigger and if it is it swaps them
def shift(array,index):
    while index > 0:
        if array[index]<array[index-1]:
            swap(array,index,index-1)
        index -=1

#calls shift for all values from 1-len(array)
def insertion_sort(array):
    for index in range(1,len(array)):
        shift(array,index)

#takes array and index and sorts all items from index and up
def insertion_sort_backwards(array,index = None):
    #if index none then index = len array -2
    if index == None:
        index = len(array)-2
    #otherwise index - 1
    else:
        index -= 1
    #ind = len array -1 aka last index
    ind = len(array)-1
    #while ind is greater than index
    while ind > index:
        #if the array at index is greater than ind then they wap and ind is -1
        if array[index]>array[ind]:
            swap(array,index,ind)
        ind -=1
    #print here to print every line
    print(array)
    #while index is greater than 0 it recalls this function with a new starting index 
    if index > 0:
        insertion_sort_backwards(array,index)


#main
def main():
    aray = arrays.Array(5)
    aray[0] = 5
    aray[1] = 3
    aray[2] = 7
    aray[3] = 1
    aray[4] = 4
    insertion_sort_backwards(aray)
    sort_col("./data/dataset.csv",2,189)
    sort_col("./data/dataset.csv",7,189)


main()