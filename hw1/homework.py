"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List
from string import ascii_lowercase


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return first is second


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError
    Raises:
        ValueError
    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if type(first_value) == int and type(second_value) == int:
        return first_value * second_value
    else:
        raise ValueError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException
    Args:
        first_value: number for multiply
        second_value: number for multiply
    Raises:
        OurAwesomeException
    Returns: multiple of two numbers.
    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    """
    if type(first_value) != enumerate and type(second_value) != enumerate:
        return int(first_value) * int(second_value)
    else:
        raise ValueError
    """
    """
    try:
        int(first_value) and int(second_value)
    except ValueError:
        raise ValueError
    """
    return int(first_value) * int(second_value)


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.
    Args:
        word: Searchable substring
        text: Text for searching
    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False
    """
    return text.find(word) != -1


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    my_list = []
    for i in range(13):
        if i != 6 and i != 7:
            my_list.append(i)
    return my_list


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    new_list = []
    for i in data:
        if i >= 0:
            new_list.append(i)
    return new_list


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """

    """
    alphabet_dict = {}
    for i in range(1, 27):
        alphabet_dict.update({i: chr(i + 96)})
    return alphabet_dict
    """
    return {ord(c) - 96: c for c in ascii_lowercase}


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:
    """
    length = len(data)
    for i in range(length - 1):
        for j in range(length - i -1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
    """
    return sorted(data)
    """
