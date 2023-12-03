"""
Make node class
Author: Ryan Robison
"""

class Node:
    __slots__ = ["__value","__next"]

    def __init__(self,value,next = None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value
    def get_next(self):
        return self.__next

def print_node(nodes):
    if nodes == None:
        return ""
    else:
        print(nodes.get_value(),end = ", ")
        print_node(nodes.get_next())