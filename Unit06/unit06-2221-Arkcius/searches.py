"""
Purpose to search arrays
Author: Ryan Robison
"""

import arrays
import array_utils
import math

def linear_search(an_array,target,start=None,end=None):
    #if statments for if end and start are out of range and to reset them
    if end == None or end > len(an_array):
        end = len(an_array)
    if start == None or start < 0:
        start = 0
    #searches in block for end minus start
    for index in range(start,end):
        if index == 0:
            index = start
        if an_array[index] == target:
            return index
    return None

def linear_search_timer():
    #told to leave blank
    return None

def print_odds(an_array):
    for index in range(len(an_array)):
        if an_array[index] % 2 == 1:
            print(an_array[index], end=" ")
    print()

def print_odds_rec(an_array, index = 0):
    if an_array[index] % 2 == 1:
        print(an_array[index],end = " ")
    if index < len(an_array)-1:
        print_odds_rec(an_array,index+1)
    else:
        print()

def jump_search(array,target):
    jump = int(math.sqrt(len(array)))
    start = 0
    end = jump
    returnal = False
    while returnal == False:
        search = linear_search(array,target,start,end)
        if search != None:
            return search
        start += jump
        end += jump
        if start > len(array):
            return None

def binary_search(array,target,start = None,end = None):
    if start == None:
        start = 0
    if end == None:
        end = len(array)
    while start <= end:
        mid = (start+end)//2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            start = mid + 1
        elif target < array[mid]:
            end = mid - 1
        binary_search(array,target,start,end)

def main():
    an_array = array_utils.range_array(1,101)
    """
    print_odds(an_array)
    print_odds_rec(an_array)
    print("found 1 at index ",linear_search(an_array,1))
    print("found 101 at index ",linear_search(an_array,101))
    """

#main()