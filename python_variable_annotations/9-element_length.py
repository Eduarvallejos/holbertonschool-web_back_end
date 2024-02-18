#!/usr/bin/env python3
"""
Defines a function that calculates the length of
each element in the given iterable
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence]]:
    """
    Function to calculate the length of each element in the given iterable.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequences.

    Returns:
        List[Tuple[Sequence]]: A list of tuples where each tuple contains
        a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
