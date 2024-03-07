#!/usr/bin/env python3
"""
This script calculates the start and end indexes for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for pagination.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start index and end index.
    """
    start_indx = (page - 1) * page_size
    end_indx = start_indx + page_size
    return start_indx, end_indx
