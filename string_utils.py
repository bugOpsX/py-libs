"""
Feature: String Utilities
Description:
Provides helpful string functions like reversing, counting vowels, and checking palindromes.
"""

def reverse_string(text: str) -> str:
    """
    Reverse the input string.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.

    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def count_vowels(text: str) -> int:
    """
    Count the number of vowels in the input string.

    Args:
        text (str): Input string.

    Returns:
        int: Number of vowels (a, e, i, o, u) in the string.

    Example:
        >>> count_vowels("hello")
        2
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def is_palindrome(text: str) -> bool:
    """
    Check if the input string is a palindrome.

    Args:
        text (str): Input string.

    Returns:
        bool: True if palindrome, False otherwise.

    Example:
        >>> is_palindrome("level")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]