"""
Purpose to test Cross_maker
Author: Ryan Robison
"""
import cross_maker

def valid_test():
    expectT = True
    expectF = False
    test1 = cross_maker.valid(0,0,"Hello",True)
    test2 = cross_maker.valid(17,0,"Hello",True)
    test3 = cross_maker.valid(0,17,"hello",False)
    assert (expectT == test1)
    assert (expectT == test2)
    assert (expectF == test3)