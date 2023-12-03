"""
Purpose to do activities
Author: Ryan Robison
"""
import arrays
import time
import random
import math
import re

def unique_array(array,value):
    for i in range(len(array)):
        current = array[i]
        if current == None:
            array[i] = value
            break
        elif current == value:
            return

def fill_array(length):
    aray = arrays.Array(length,None)
    start = time.perf_counter()
    for value in range(length):
        unique_array(aray,value)
    return round(time.perf_counter()-start,3)

def unique_list(lista,value):
    for i in range(len(lista)):
        if lista[i]==value:
            return
    lista.append(value)

def fill_list(length):
    lista = []
    start = time.perf_counter()
    for i in range(length):
        unique_list(lista,i)
    return round(time.perf_counter()-start,4)

def coupon_collector(n):
    collection = set()
    boxes = 0
    while len(collection)<n:
        r = random.randint(1,n)
        collection.add(r)
        boxes += 1
    return boxes

def mixup():
    stringa = "abcdefghijklmnopqrstuvwxyz"
    seta = set(stringa)
    for char in seta:
        print(char,end = " ")
    print()
    print(seta)

def sets():
        seta = {1,2,3,4}
        print(seta)
        seta.add(5)
        seta.add(7)
        print(seta)
        for i in seta:
            print(i,end = " ")
        print()
        setb = set("abcddcbaabcde")
        print(setb)

def unique_words(filename):
    seta = set()
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                real_words = re.findall("[\w]+",word.lower())
                for real_word in real_words:
                    seta.add(real_word)
    return seta

def names():
    names = {}
    names["K"] = "Kennedy1"
    names["J"] = "Jack"
    names["L"] = "Lee"
    names["K"] = "Kennedy2"
    print(names)
    print(names["L"])


def main():
    names()


main()