"""
Purpose to do practical 9
Author: Ryan Robison
"""
#takes in list and revereses it without storing value
def in_place_reverse(lista):
    #for i in range lenght -1 it inserts the poped value to the current ind
    for i in range(len(lista)-1):
        lista.insert(i,lista.pop())
    return lista

#makes list long way
def make_multiplication_table():
    lista = []
    #makes empty list and for loop
    for i in range(10):
        #makes new empty list each loop
        listb = []
        for j in range(10):
            #makes calculations for 1-10 and plugs into second list
            listb.append((i+1)*(j+1))
        #adds second list to first list
        lista.append(listb)
    return lista

#does same as above but in one line aka makes a list of lists for i*j
def make_multiplication_table2():
    return[[i*q for i in range(1,11)] for q in range(1,11)]

def main():
    lista = [1,2,3,4,5,6]
    print(lista)
    print(in_place_reverse(lista))
    listb = make_multiplication_table()
    for i in range(10):
        print(listb[i])
    listc = make_multiplication_table2()
    for i in range(10):
        print(listc[i])

    

main()