
import pytest 
from src import string
day = 30

#@pytest.mark.skip(reason="this feature is not ready yet")
@pytest.mark.skipif(day <= 28, reason="this feature shall run starting from day 28 of each month")
def test_reverse_string():
    assert string.reverse_string("hello") == "olleh"
    assert string.reverse_string("Python") == "nohtyP"
    assert string.reverse_string("ahmed") == "demha"

@pytest.mark.RAMADN_RELEASE
def test_is_plindrome():
    assert string.is_plindrome("level") == True
    assert string.is_plindrome("madam") == True
    assert string.is_plindrome("racecar") == True
    assert string.is_plindrome("iti") == True
    assert string.is_plindrome("hello") == False

def test_count_vowels():
    assert string.count_vowels("hello") == 2
    assert string.count_vowels("Python") == 1
    assert string.count_vowels("ahmed") == 2

def test_is_uppercase():
    assert string.is_uppercase("HELLO") == True
    assert string.is_uppercase("Python") == False
    assert string.is_uppercase("AHMED") == True
    
@pytest.mark.RAMADN_RELEASE
def test_is_lowercase():
    assert string.is_lowercase("hello") == True
    assert string.is_lowercase("PYTHON") == False
    assert string.is_lowercase("ahmed") == True
    