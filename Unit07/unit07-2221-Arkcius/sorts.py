"""
Purpose to make sorting 
Author: Ryan Robison
"""
import array_utils
import arrays

def swap(array,a,b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def shift(array,index):
    while index > 0:
        if array[index]<array[index-1]:
            swap(array,index,index-1)
        index -=1

def shift_wo_swap(array,index):
    target = array[index]
    target_index = index
    while target_index > 0 and target<array[target_index-1]:
        array[target_index] = array[target_index-1]
        target_index -=1
    array[target_index] = target


def insertion_sort(array):
    for index in range(1,len(array)):
        shift(array,index)

def insertion_sort_wo(array):
    for index in range(1,len(array)):
        shift_wo_swap(array,index)

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


def main():
    araay = arrays.Array(5)
    araay[0] = 5
    araay[1] = 3
    araay[2] = 7
    araay[3] = 1
    araay[4] = 4
    insertion_sort_backwards(araay)
    aray = array_utils.random_array(10)
    print(aray)
    insertion_sort(aray)
    print(aray)
    array = array_utils.random_array(10)
    print(array)
    insertion_sort_wo(array)
    print(array)


main()
