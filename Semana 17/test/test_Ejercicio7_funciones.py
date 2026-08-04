from code2test.Ejercicio7 import calculate_prime_numbers

def test_calculate_prime_numbers_short_list():
    #Arrange
    prime_list = [24, 12, 1, 7]
    #ACT
    result = calculate_prime_numbers(prime_list)
    #Assert
    assert result == [1, 7]

def test_calculate_prime_numbers_with_no_prime_in_list():
    #Arrange
    prime_list = [24, 12, 15, 72]
    #ACT
    result = calculate_prime_numbers(prime_list)
    #Assert
    assert result == []

def test_calculate_prime_numbers_empy_list():
    #Arrange
    prime_list = []
    #ACT
    result = calculate_prime_numbers(prime_list)
    #Assert
    assert result == []
