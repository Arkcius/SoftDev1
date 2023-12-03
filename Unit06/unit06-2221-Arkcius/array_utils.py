"""
Purpose to use arrays and random
Author: Ryan Robison
"""
import arrays
import random

def random_array(size,min_val = 0,max_val = None):
    aray = arrays.Array(size,0)
    if max_val == None:
        max_val = size
    for index in range(size):
        aray[index] = random.randint(min_val,max_val)
    return aray

def range_array(start,stop,step = 1):
    arange = range(start,stop,step)
    length = len(arange)
    anarray = arrays.Array(length,0)
    for index in range(length):
        anarray[index] = arange[index]
    return anarray

def main():
    print(range_array(1,10))
    aray = random_array(10)
    print(aray)
        
main()