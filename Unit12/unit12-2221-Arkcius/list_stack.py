"""
Make list stack
Author: Ryan Robison
"""

#node class
class Node:
    #slots for value and next
    __slots__ = ["__value","__next"]

#initialize with vaule and next is naturally none unless given
    def __init__(self,value,next = None):
        self.__value = value
        self.__next = next

#returns next and value
    def get_value(self):
        return self.__value
    def get_next(self):
        return self.__next

#stack class
class Stack:
    #slots for size and top
    __slots__ = ["__size","__top"]

#initialize with size = 0 and top as none
    def __init__(self):
        self.__size = 0
        self.__top = None
#returns if empty
    def is_empty(self):
        return self.__top == None
#adds new node value to top
    def push(self,value):
        new_node = Node(value,self.__top)
        self.__top = new_node
        self.__size += 1

#checks top valiue
    def peek(self):
        return self.__top.get_value()

#takes off top value
    def pop(self):
        value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return value

#if node next is none returns none and otherwise returns getstring of next and the value
    def get_string(self,node):
        if node == None:
            return ""
        else:
            return self.get_string(node.get_next()) + str(node.get_value()) +","

#prints the string from get string and if stack not empty adds the top value
    def __repr__(self):
        string = self.get_string(self.__top) 
        if self.__top != None:
            string += self.__top.get_value()
        return "["+string[:-2]+"]"

#tests
def main():
    astack = Stack()
    print(astack.is_empty())
    print(repr(astack))
    astack.push("a")
    astack.push("b")
    astack.push("d")
    print(repr(astack))
    astack.pop()
    astack.pop()
    print(repr(astack))
    print(astack.peek())

main()