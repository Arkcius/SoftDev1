"""
Various useful array utilities. Provided for use on the homework in this unit.

@author GCCIS Faculty - modified by students.
"""

import arrays
import random

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def copy_array(an_array, length = None):
    if length == None:
        length = len(an_array)
    copy = arrays.Array(length)
    for i in range(length):
        copy[i] = an_array[i]
    return copy

def cat_array(a1, a2):
    result = arrays.Array(len(a1)+len(a2))
    for i in range(len(a1)):
        result[i] = a1[i]
    for i in range(len(a1), len(result)):
        result[i] = a2[i-len(a1)]
    return result

def increasing_comparator(a, b):
    return a <= b

#decreasing comparator comparing if b is less than or equal to a
def decreasing_comparator(a,b):
    return b <= a

#is sorted function takes array and comparator 
def is_sorted(an_array,comparator = increasing_comparator):
    #set sorted to originally true
    sorted = True
    #for all ind in range length -1
    for ind in range(len(an_array)-1):
        #checks if array ind is compared to array ind+1 with the comparator given
        sort = comparator(an_array[ind],an_array[ind+1])
        #if sort == false at any time sets sorted to false
        if sort == False:
            sorted = False
    #returns sorted
    return sorted

def main():
    random.seed(1)
    aray = arrays.Array(3)
    aray[0] = 30
    aray[1] = 20
    aray[2] = 10
    print(is_sorted(aray,decreasing_comparator))
    print(is_sorted(aray))
    array = arrays.Array(3)
    array[0] = 20
    array[1] = 20
    array[2] = 30
    print(is_sorted(array))
    print(is_sorted(array,decreasing_comparator))

if __name__ == "__main__":
    main()
