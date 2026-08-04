from code2test.Extra2 import divide
import pytest

def test_divide_normal_case():
    #Arrange
    num1 = 10
    num2 = 2
    #ACT
    result = divide(num1, num2)
    #Assert
    assert result == 5

def test_divide_by_zero_case():
    #Arrange
    num1 = 10
    num2 = 0
    #ACT & Assert
    with pytest.raises(ValueError):
        divide(num1, num2)

def test_divide_with_string_as_parameter():
    #Arrange
    num1 = "some_words"
    num2 = 5
    #ACT & Assert
    with pytest.raises(TypeError):
        divide(num1, num2)