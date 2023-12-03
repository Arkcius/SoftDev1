"""
stack main
Author:Ryan Robison
"""
from node_stack import *

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