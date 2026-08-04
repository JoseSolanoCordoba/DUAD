from code2test.Ejercicio6 import ordering_words
import string

def test_ordering_words_short_string():
    #Arrange
    short_string = "sky-moon-plane"
    #ACT
    result = ordering_words(short_string)
    #Assert
    assert result == "moon-plane-sky"

def test_ordering_words_upper_and_lowercase_string():
    #Arrange
    short_string = "sky-Moon-plane-Generator"
    #ACT
    result = ordering_words(short_string)
    #Assert
    assert result == "Generator-Moon-plane-sky"

def test_ordering_words_empy_string():
    #Arrange
    short_string = ""
    #ACT
    result = ordering_words(short_string)
    #Assert
    assert result == ""
