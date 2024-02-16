#!/usr/bin/env python3
"""
This script defines a type-annotated function 'sum_list'
that takes an 'imput_list' list of floats as arguments and
returns a sum as a float
"""
from typing import List


def sum_list(imput_list: List[float]) -> float:
    """
    Calculate the sum of floats in the input list.

    Args:
        input_list (List[float]): List of floats to sum.

    Returns:
        float: Sum of the input_list.
    """
    return sum(imput_list)
