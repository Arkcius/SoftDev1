"""
purpose to use tuples
Author: Ryan Robison
"""
import random
import arrays
import array_utils

def tuples(tuplea):
    print(len(tuplea))
    print(tuplea)
    for element in tuplea:
        print(element)

def lists():
    lista = [1,2,"a",True,(1,2)]
    for element in lista:
        print(element)
    lista[0] = 57
    return lista

def list2():
    lista = [1,2,"a",True,(1,2)]
    for ind in range(len(lista)):
        print(ind, ": ",lista[ind], sep = "")
    lista[0] = 57
    return lista

def make_list(asequence):
    lista = []
    for elements in asequence:
        lista.append(elements)
        print(lista)
    return lista

def scale(lista,scalar):
    for ind in range(len(lista)):
        lista[ind] = lista[ind]*scalar
    return lista

def mutater(alist,aint):
    print(alist)
    print(aint)
    aint = aint * 5
    alist[0] *= 5
    print(alist)
    print(aint)

def cat(alist,blist):
    clist = alist+blist
    return clist

def extender(lista,listb):
    lista += listb
    return lista

def inserter(lista,inta):
    mid = len(lista)//2
    lista.insert(mid,inta)

def popper(lista):
    length = len(lista)
    if length > 0:
        ind = random.randrange(length)
        pop = lista.pop(ind)
        print(lista,pop)
        popper(lista)

def array_insert(array,index,value):
    length = len(array)
    if length == 0:
        return arrays.Array(1,value)
    else:
        inserted = arrays.Array(length+1)
        for i in range(index):
            inserted[i] = array[i]
        inserted[index]=value
        for i in range(index+1,length+1):
            inserted[i]=array[i-1]
        return inserted

def array_pop(array,index):
    length = len(array)
    popped = arrays.Array(length-1)
    for i in range(index):
        popped[i]=array[i]
    for i in range(index+1,length):
        popped[i-1]=array[i]
    return popped, array[index]

def rgb_tuble():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)

def tuple_equality(a_tuple, b_tuple):
    print(a_tuple)
    print(b_tuple)
    print(a_tuple is b_tuple)
    print(a_tuple == b_tuple)
    print()
def reverse_sequence(sequence):
    lst = []
    length = len(sequence)
    for index in range(length-1, -1, -1):
        lst.append(sequence[index])

    return lst

def slices():
    a_string = "Does my password begin with a one or a two?"
    a_list = list(a_string)
    start = 0
    stop = 0
    for index in range(len(a_list)):
        if a_list[index] == ' ':
            stop = index
            word = a_list[start:stop]
            print(word)
            start = stop + 1
    # the last word
    word = a_list[start:]
    print(word)

def dices(a_list):
    if not a_list:
        return
    else:
        index = random.randrange(len(a_list))
        element = a_list[index:index+1]
        print(element)
        new_list = a_list[:index] + a_list[index + 1:]
        dices(new_list)

def random_list(size):
    randlist = []
    for _ in range(size):
        value = random.randint(0,100)
        randlist.append(value)
    return randlist

def sorted_test(list, backwards = False):
    print("Before: ",list)
    blist = sorted(list, reverse=backwards)
    print("After: ",list)
    print("Sorted",blist)

def sort_test(list,backwards = False):
    print("Before: ",list)
    list.sort(reverse = backwards)
    print("After: ",list)

def sort_cards(hand):
    print(hand)
    hand.sort(key = suit_key)
    print(hand)

def suit_key(card):
    key = 0
    suit = card[1]
    if suit == "D":
        key+=100
    elif suit == "H":
        key+=200
    elif suit == "S":
        key += 300
    key += card[0]
    return key

def packer():
    return 1,"abc",True,5

def swapper(lista):
    length=len(lista)
    if length < 2:
        return lista
    else:
        half = length//2
        swapped = []
        for index in range(half,length):
            swapped.append(lista[index])
        for index in range(half):
            swapped.append(lista[index])
        return swapped

def chunky(lista,size):
    start = 0
    stop = size
    chunk = lista[start:stop]
    while chunk:
        print(chunk)
        start = stop
        stop = start + size
        chunk = lista[start:stop]


def sevens_key(number):
    key = 0
    strings = str(number)
    if strings[0] == "7":
        key += 0
    else:
        key += 200
    key += number
    return key

def lucky_7(lista):
    print(lista)
    lista.sort(key = sevens_key)
    print(lista)

def main():
    hand = [(5,"H"), (8,"D"), (10,"S"), (2,"D"), (7,"H")]
    sort_cards(hand)

    swapp = [1,2,3,4,5,6,7,8,9,]
    print(swapp)
    chunky(swapp,3)
    listb = [value for value in range(0,100,7)]
    lista = random_list(20)
    lucky_7(lista)
    lucky_7(listb)


main()