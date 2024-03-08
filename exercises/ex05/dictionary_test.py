"""Testing functionality of functions from EX05."""
__author__ = "730487065"
import pytest
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_grade_invert() -> None:  # Expected use case.
    """Testing functionality when inverting lists of grades."""
    input_dict = {'A': 'ninety', 'B': 'eighty', 'C': 'seventy'}
    output_dict = {'ninety': 'A', 'eighty': 'B', 'seventy': 'C'}
    assert invert(input_dict) == output_dict


def test_invert_basic() -> None:  # Use case. Making sure invert works as expected. 
    """Testing functionality of invert function."""
    input_dict = {"a": "1", "b": "2", "c": "3"}
    output_dict = {"1": "a", "2": "b", "3": "c"}
    assert invert(input_dict) == output_dict


def test_invert_duplicate_vals() -> None:  # Edge case. Testing response for inputting suplicate values (when returned they would be Keys, and you cant have two of the same key).
    """Test with duplicate values."""
    input_dict = {"a": "1", "b": "2", "c": "1"}
    with pytest.raises(KeyError):
        invert(input_dict)


def test_empty_fav_color() -> None:  # Edge case. 
    """Testing that favorite color returns empty string if dictionary is empty."""
    assert favorite_color({}) == ""


def test_single_fav_color() -> None:  # Use case to test single fav color functionality.
    """Testing basic functionality of single favorite color in function."""
    color_dict = {'Ella': 'blue'}
    assert favorite_color(color_dict) == 'blue'


def test_multiple_fav_colors() -> None:  # Use case to test multiple favorite colors.
    """Testing functionality when multiple favorite colors are input."""
    color_dict = {'Ella': 'blue', 'Grayson': 'green', 'Kyla': 'pink', 'Roman': 'green'}
    assert favorite_color(color_dict) == 'green'


def test_empty_dict_count() -> None:  # Edge case.
    """Testing when empty list is input into count function- return empty dict."""
    freq_list = []
    assert count(freq_list) == {}


def test_appear_once_count() -> None:  # Expected use case. 
    """Function to test when each item only appears once."""
    freq_list = ['horse', 'cow', 'bird', 'iguana', 'emu', 'octopus']
    assert count(freq_list) == {'horse': 1, 'cow': 1, 'bird': 1, 'iguana': 1, 'emu': 1, 'octopus': 1}


def test_appear_multiple_count() -> None:  # Expected use case.
    """Function to test functionality when items appear multiple times."""
    freq_list = ['horse', 'cow', 'horse', 'dog', 'dog', 'dog', 'horse', 'horse']
    assert count(freq_list) == {'horse': 4, 'cow': 1, 'dog': 3}


def test_empty_alphabetizer() -> None:  # Edge Case.
    """Function to test that alphabetizer returns empty dictionary when empty list is input."""
    words = []
    assert alphabetizer(words) == {}


def test_alph_one_letter() -> None:  # Expected use case.
    """Function to test functionality when there is only one word for each letter of the alphabet."""
    words = ['apple', 'banana', 'carrot', 'dill', 'eggplant', 'fennel']
    assert alphabetizer(words) == {'a': ['apple'], 'b': ['banana'], 'c': ['carrot'], 'd': ['dill'], 'e': ['eggplant'], 'f': ['fennel']}


def test_alph_multiple_same() -> None:  # Expected use case.
    """Function to test functionality when multiple words start with the same letter of the alphabet."""
    words = ['apple', 'banana', 'asparagus', 'arugula', 'blackberry', 'carrot', 'dill', 'corn', 'eggplant', 'fennel']
    assert alphabetizer(words) == {'a': ['apple', 'asparagus', 'arugula'], 'b': ['banana', 'blackberry'], 'c': ['carrot', 'corn'], 'd': ['dill'], 'e': ['eggplant'], 'f': ['fennel']}


def test_no_students_attendance() -> None:  # Edge Case.
    """Function to test functionality if the school has no students."""
    exist_dict = {}  # empty dict
    day = ''  # empty string
    student = ''  # empty string 
    update_attendance(exist_dict, day, student)  # Returns none 
    assert exist_dict == {'': ['']}


def test_one_day_attendance() -> None:  # Expected use case.
    """Function to test functionality of appending attendance for one day from empty dict."""
    exist_dict = {}
    day = 'Monday'
    student = 'Ella'
    update_attendance(exist_dict, day, student)
    assert exist_dict[day] == ['Ella']
    assert exist_dict['Monday'] == ['Ella']


def test_multiple_day_attendance() -> None:  # Expected use case.
    """Function to test functionality when days already exist in dictionary."""
    exist_dict = {'Monday': ['Ella', 'Grayson'], 'Tuesday': ['Kyla', 'Grayson'], 'Wednesday': ['Ella', 'Kyla']}
    day = 'Tuesday'
    student = 'Ella'
    update_attendance(exist_dict, day, student)
    assert exist_dict[day] == ['Kyla', 'Grayson', 'Ella']
    assert exist_dict['Tuesday'] == ['Kyla', 'Grayson', 'Ella']