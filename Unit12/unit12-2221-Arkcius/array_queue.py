"""
array queue
Author: Ryan Robison
"""
import arrays

class Queue:
    __slots__ = ["__front","__back","__size","__array"]

    def __init__(self,capacity = 3):
        self.__array = arrays.Array(capacity)
        self.__front =0
        self.__back = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def size(self):
        return self.__size

    def __repr__(self):
        string = ''
        i = self.__front
        if self.__size > 0:
            string += str(self.__array[i]) + ', '
            i = (i+1)%len(self.__array)
        while i != self.__back:
            string += str(self.__array[i]) + ', '
            i = (i+1)%len(self.__array)
        return '['+string[:-2]+']'

    def enqueue(self,value):
        self.__array[self.__back] = value
        self.__back = (self.__back + 1) % len(self.__array)
        self.__size += 1
        if self.__back == self.__front:
            self.__resize()
    
    def get_back(self):
        return self.__array[self.__back-1]
    def get_front(self):
        return self.__array[self.__front]

    def dequeue(self):
        if self.__size <= 0:
            raise IndexError ("Cannot as queue is empty")
        value = self.__array[self.__front]
        self.__front = (self.__front +1)%len(self.__array)
        self.__size -= 1
        return value
    
    def __resize(self):
        new = arrays.Array(len(self.__array)*2+1)
        i = self.__front
        j = 0
        for _ in range(self.__size):
            new[j] = self.__array[i]
            i = (i+1)%len(self.__array)
            j += 1

        self.__front = 0
        self.__back = j
        self.__array = new

def main():
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(4)
    print(q)
    q.enqueue(7)
    print(q)

main()