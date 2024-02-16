#!/usr/bin/env python3
"""
Defining a function to sum elements of a mixed list of integers and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Adds the elements of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and
        floats.

    Returns:
        float: The sum of the list elements as a floating number.
    """
    return sum(mxd_lst)
