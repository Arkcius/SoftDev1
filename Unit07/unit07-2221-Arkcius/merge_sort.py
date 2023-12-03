"""
Purpose to make a merge sort
Author: Ryan Robison
"""
import arrays
import array_utils


def splitter(array):
    evens = arrays.Array((len(array)+1)//2)
    odds = arrays.Array(len(array)//2)
    ev = 0
    od = 0
    for index in range(len(array)):
        if index %2 == 0:
            evens[ev] = array[index]
            ev+=1
        elif index %2 == 1:
            odds[od]= array[index]
            od+=1
    return evens, odds

def merge(array1,array2):
    length = len(array1)+len(array2)
    combined = arrays.Array(length)
    ind1 = 0
    ind2 = 0
    while ind1 < len(array1) and ind2 < len(array2):
        if array1[ind1] <= array2[ind2]:
            combined[ind1+ind2] = array1[ind1]
            ind1 += 1
        else:
            combined[ind1+ind2]=array2[ind2]
            ind2+=1
    if ind1 < len(array1):
        for ind in range(ind1,len(array1)):
            combined[ind+ind2] = array1[ind]
    if ind2 < len(array2):
        for ind in range(ind2,len(array2)):
            combined[ind+ind1] = array2[ind]
    return combined
    

def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        (half1,half2) = splitter(array)
        return merge(merge_sort(half1),merge_sort(half2))   


def main():
    array = arrays.Array(10)
    array[0] = 1
    array[1] = 5
    array[2] = 18
    array[3] = 3
    array[4] = 9
    array[5] = 1
    array[6] = 5
    array[7] = 18
    array[8] = 3
    array[9] = 9
    print(array)
    print(splitter(array))
    result = merge_sort(array)
    print(result)

main()