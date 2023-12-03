"""
stack main
Author: Ryan Robison
"""
from node import *

def main():
    stack = Node(5)
    stack2 = Node(2,stack)
    stack3 = Node(4,stack2)
    stack4 = Node(7,stack3)
    s = stack.get_value()
    s2 = stack2.get_value()
    print(s)
    print(s2)
    print_node(stack4)

main()