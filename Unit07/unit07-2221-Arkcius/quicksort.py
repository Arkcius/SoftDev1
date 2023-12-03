"""
Purpose to make a quicksort algorithm
Author: Ryan Robison
"""
import arrays
import array_utils

def quick_sort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less, same, more = partition(pivot,array)
        aray = cat(quick_sort(less),same)
        aray = cat(aray,quick_sort(more))
        return aray

def partition(pivot,array):
    samecount = 0
    lesscount = 0
    morecount = 0
    inds = 0
    indl = 0
    indm = 0
    for ind in range(len(array)):
        if array[ind] == pivot:
            samecount += 1
        elif array[ind] < pivot:
            lesscount +=1
        elif array[ind] > pivot:
            morecount += 1
    less = arrays.Array(lesscount)
    more = arrays.Array(morecount)
    same = arrays.Array(samecount)
    for ind in range(len(array)):
        if array[ind] == pivot:
            same[inds] = array[ind]
            inds += 1
        elif array[ind] < pivot:
            less[indl] = array[ind]
            indl += 1
        elif array[ind] > pivot:
            more[indm] = array[ind]
            indm+= 1
    return less, same, more

def cat(array1,array2):
    lengtha = len(array1)
    lengthb = len(array2)
    array = arrays.Array(lengtha+lengthb)
    for ind in range(lengtha):
        array[ind] = array1[ind]
    for ind in range(lengtha,len(array)):
        array[ind] = array2[ind-lengtha]
    return array


#for the HW 7.2 mr hill said to not worry about times which includes 1-3 and 5 so im assuming were just supposed to do part 4 which is below
#
def quick_insertion_sort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less, same, more = partition(pivot,array)
        #makes a variable for the floor of more times 3
        mo = (len(more)//3)*3
        #checks if values of more in more both throughout and the first 3 are in order and if less length is less than 2
        if len(more)>3:
            Morex = (more[0]<=more[1]<=more[2] and more[0]<=more[int(mo/3)]<=more[int(mo/3*2)]) and len(less)<=2
        #if met then performs insertion sort for more and less
        if Morex == True:
            aray = cat(insertion_sort(less),same)
            aray = cat(aray,insertion_sort(more))
            return aray
        aray = cat(quick_sort(less),same)
        aray = cat(aray,quick_sort(more))
        return aray

#basic insertion sort
def swap(array,a,b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def shift(array,index):
    while index > 0:
        if array[index]<array[index-1]:
            swap(array,index,index-1)
        index -=1

def insertion_sort(array):
    for index in range(1,len(array)):
        shift(array,index)
    return array

def main():
    aray = array_utils.random_array(100)
    arayy = array_utils.range_array(1,100)
    print(arayy)
    print(quick_insertion_sort(arayy))
    print(aray)
    print(quick_sort(aray))
    

main()