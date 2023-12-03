"""
Purpose to test search
Author: Ryan Robison
"""


import searches
import array_utils

#test for searching normally
def test_normal():
    aray = array_utils.range_array(1,101)
    expected = 5
    index = searches.linear_search(aray,5)
    actual = aray[index]
    assert actual == expected

#test for seraching out of array
def test_outof():
    aray = array_utils.range_array(1,101)
    expected = None
    index = searches.linear_search(aray,-1)

    assert expected == index

#test for if variable under search and if it works when end out of range
def test_start_end():
    aray = array_utils.range_array(1,10)
    expected = None
    index = searches.linear_search(aray,5,7,12)
    actual = index
    assert actual == expected

#test for if variable after search area
def test_start_end2():
    aray = array_utils.range_array(1,10)
    expected = None
    index = searches.linear_search(aray,5,0,3)
    actual = index
    assert actual == expected

#test to make sure it all works
def test_start_end3():
    aray = array_utils.range_array(1,10)
    expected = 9
    index = searches.linear_search(aray,9,3,12)
    actual = aray[index]
    assert actual == expected

#test jump normally
def test_jump():
    aray = array_utils.range_array(1,10)
    expected = 9
    index = searches.jump_search(aray,9)
    assert aray[index] == expected

#test if jump when target over
def test_jump2():
    aray = array_utils.range_array(1,10)
    expected = None
    index = searches.jump_search(aray,11)
    assert index == expected

#test jump when target under
def test_jump3():
    aray = array_utils.range_array(1,10)
    expected = None
    index = searches.jump_search(aray,-3)
    assert index == expected

#test binary normal
def test_binary1():
    aray = array_utils.range_array(1,10)
    expected = 9
    index = searches.binary_search(aray,9)
    assert aray[index] == expected

#test binary under
def test_binary2():
    aray = array_utils.range_array(1,10)
    expected = None
    index = searches.binary_search(aray,-3)
    assert index == expected

#test binary over
def test_binary3():
    aray = array_utils.range_array(1,10)
    expected = None
    index = searches.binary_search(aray,12)
    assert index == expected

def main():
    test_normal()
    test_outof()
    test_start_end()
    test_start_end2()
    test_start_end3()
    test_jump()
    test_jump2()
    test_jump3()
    test_binary1()
    test_binary2()
    test_binary3()

main()