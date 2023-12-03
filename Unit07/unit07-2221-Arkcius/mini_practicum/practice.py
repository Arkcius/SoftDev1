"""
Purpose to find max and power
Author: Ryan Robison
"""
import array_utils

#function to find max value in a function
def max(array,index = 0,maxx=None):
    #if the array is length 0 return None
    if len(array)==0:
        return None
    #if maxx is none initially sets it to first array index
    if maxx == None:
        maxx = array[0]
    #if the maxx is less than array at index makes maxx that value
    elif maxx<array[index]:
            maxx = array[index]
    #if index is less than array lenght calls function again
    if index < len(array)-1:
        maxx = max(array,index+1,maxx)
    return maxx

#takes in base and exponent and returns value
def power(base,exponent):
    #if the exponent less than 0 raises valueerror
    if exponent < 0:
        raise ValueError
    #if exponent = 0 returns 1
    if exponent == 0:
        return 1
    #if exponent = 1 returns base
    if exponent == 1:
        return base
    #if exponent odd solves using recursion
    if exponent % 2 == 1:
        return (base * power(base,exponent//2)*power(base,exponent//2))
    #if exponent even solves using recursion
    if exponent % 2 == 0:
        return (power(base,exponent//2)*power(base,exponent//2))

def main():
    an_array = array_utils.range_array(0,10)
    largest = max(an_array)
    print(largest)
    result = power(4,7)
    print(result)

main()