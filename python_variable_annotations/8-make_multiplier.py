#!/usr/bin/env python3
"""Function to create a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the result of multiplying it by the multiplier.
    """

    def multiplier_function(number: float) -> float:
        """
        Function that multiplies a given number by the multiplier value.

        Args:
            x (float): The number to be multiplied.

        Returns:
            float: The result of multiplying the number by the multiplier.
        """
        return number * multiplier
    return multiplier_function
