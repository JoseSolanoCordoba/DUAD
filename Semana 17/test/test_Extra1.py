from code2test.Extra1 import *

def test_sum_elements_of_list_positive_numbers():
    #Arrange
    numbers_list = [24, 12, 1, 7]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == 44

def test_sum_elements_of_list_negative_numbers():
    #Arrange
    numbers_list = [-24, -12, -1, -7]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == -44

def test_sum_elements_of_list_zeros():
    #Arrange
    numbers_list = [0, 0, 0, 0]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == 0

def test_average_of_list_positive_numbers():
    #Arrange
    numbers_list = [24, 12, 1, 7]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == 44

def test_average_of_list_negative_numbers():
    #Arrange
    numbers_list = [-24, -12, -1, -7]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == -44

def test_average_of_list_zeros():
    #Arrange
    numbers_list = [0, 0, 0, 0]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == 0

def test_max_element_of_list_positive_numbers():
    #Arrange
    numbers_list = [24, 12, 1, 7]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == 44

def test_max_element_of_list_negative_numbers():
    #Arrange
    numbers_list = [-24, -12, -1, -7]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == -44

def test_max_element_of_list_zeros():
    #Arrange
    numbers_list = [0, 0, 0, 0]
    #ACT
    result = sum_elements_of_list(numbers_list)
    #Assert
    assert result == 0