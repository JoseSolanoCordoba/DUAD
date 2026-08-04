from code2test.Ejercicio3 import sum_elements_of_list

def test_sum_elements_of_list_short_lists():
    #Arrange
    list = [50, 1, 3]
    #ACT
    sum = sum_elements_of_list(list)
    #Assert
    assert sum == 54

def test_sum_elements_of_list_large_lists():
    #Arrange
    list_numbers = []
    for i in range(100, 0, -1):
        list_numbers.append(i)
    print(list_numbers)
    #ACT
    sum = sum_elements_of_list(list_numbers)
    #Assert
    expected_list = []
    for i in range(1, 101):
        expected_list.append(i)
    assert sum == 5050

def test_sum_elements_of_list_empty_list():
    #Arrange
    empty_list = []
    #ACT
    sum = sum_elements_of_list(empty_list)
    #Assert
    assert sum == 0
