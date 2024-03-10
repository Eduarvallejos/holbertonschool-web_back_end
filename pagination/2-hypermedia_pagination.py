#!/usr/bin/env python3
"""Pagination of Popular_Baby_Name.csv"""

import csv
import math
from typing import List, Dict, Any


index_range = __import__('0-simple_helper_function').index_range


def verify_enter_positive(num) -> None:
    """
    Define a function to verify that a number is a positive intege
    """
    assert isinstance(num, int) and num > 0, AssertionError


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the database.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The size of the page (default is 10).

        Returns:
            List[List]: The list of records corresponding to the
                        requested page.
        """
        # Verify that page and page_size are positive integers
        verify_enter_positive(page)
        verify_enter_positive(page_size)

        start_index, end_index = index_range(page, page_size)

        return self.dataset()[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary containing hyperlinked pagination information.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The size of the page (default is 10).

        Returns:
            dict: A dictionary containing pagination information.
        """

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
