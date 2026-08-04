from code2test.bubblesort import bubble_sort
import pytest

def test_bubble_sort_short_lists():
    #Arrange
    list = [50, 1, 3]
    #ACT
    reordered_list = bubble_sort(list)
    #Assert
    assert reordered_list == [1, 3, 50]

def test_bubble_sort_large_lists():
    #Arrange
    list_numbers = []
    for i in range(100, 0, -1):
        list_numbers.append(i)
    print(list_numbers)
    #ACT
    reordered_list = bubble_sort(list_numbers)
    #Assert
    expected_list = []
    for i in range(1, 101):
        expected_list.append(i)
    assert reordered_list == expected_list

def test_bubble_sort_empy_list():
    #Arrange
    empty_list = []
    #ACT
    reordered_list = bubble_sort(empty_list)
    #Assert
    assert reordered_list == []

def test_bubble_sort_not_a_list_input():
    #Arrange
    not_a_list = {1:"h",3:"m",4: "y"}
    #ACT & Assert
    with pytest.raises((TypeError, KeyError)):
        bubble_sort(not_a_list)