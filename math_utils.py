"""
Feature: Math Utilities
Description:
Provides reusable math functions: factorial (recursive & iterative), prime checking, GCD, and LCM.
"""

from math import gcd as math_gcd

def factorial_recursive(n: int) -> int:
    """
    Calculate factorial recursively.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.

    Example:
        >>> factorial_recursive(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial iteratively.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.

    Raises:
        ValueError: If n is negative.

    Example:
        >>> factorial_iterative(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Integer number.

    Returns:
        bool: True if prime, False otherwise.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def lcm(a: int, b: int) -> int:
    """
    Calculate LCM of two numbers.

    Args:
        a (int), b (int): Integers.

    Returns:
        int: Least Common Multiple of a and b.

    Example:
        >>> lcm(4, 6)
        12
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math_gcd(a, b)
