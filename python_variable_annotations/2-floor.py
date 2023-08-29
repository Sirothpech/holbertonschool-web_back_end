#!/usr/bin/env python3
"""This module contains a function that returns the floor of a float."""


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to the input number.

    Args:
        n (float): The input floating-point number.

    Returns:
        int: The largest integer less than or equal to the input number.

    Example:
        >>> num = 3.7
        >>> result = floor(num)
        >>> print(result)
        3
    """
    return int(n)
