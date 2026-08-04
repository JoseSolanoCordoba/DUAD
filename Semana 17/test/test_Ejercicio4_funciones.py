from code2test.Ejercicio4 import revert_string
import string

def test_revert_string_short_string():
    #Arrange
    short_string = "some words"
    #ACT
    inverted_string = revert_string(short_string)
    #Assert
    assert inverted_string == 'sdrow emos'

def test_revert_string_large_string():
    #Arrange
    alphabet = string.ascii_lowercase
    #ACT
    inverted_string = revert_string(alphabet)
    #Assert
    assert inverted_string == alphabet[::-1]

def test_revert_string_empty_string():
    #Arrange
    empty_string = ""
    #ACT
    result = revert_string(empty_string)
    #Assert
    assert result == ""
