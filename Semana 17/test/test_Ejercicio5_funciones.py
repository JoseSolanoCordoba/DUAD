from code2test.Ejercicio5 import case_evaluation
import string

def test_case_evaluation_short_string():
    #Arrange
    short_string = "AabC"
    #ACT
    upper, lower = case_evaluation(short_string)
    #Assert
    assert upper == 2 and lower == 2

def test_case_evaluation_large_string():
    #Arrange
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    #ACT
    upper, lower = case_evaluation(alphabet)
    #Assert
    assert upper == 26 and lower == 26

def test_case_evaluation_empy_string():
    #Arrange
    empty_string = ""
    #ACT
    upper, lower = case_evaluation(empty_string)
    #Assert
    assert upper == 0 and lower == 0
