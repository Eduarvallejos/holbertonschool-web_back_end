#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns the requested pagination along with hypermedia
        considering data deletion.

        Args:
            index (int): Page number.
            page_size (int): Number of items per page.

        Returns:
            dict: With the hypermedia of the requested pagination.
        """
        assert index < len(self.__indexed_dataset), AssertionError

        n = 0
        end_index = index + page_size
        next_index = end_index
        data = []

        for i in range(index, end_index):
            item = self.__indexed_dataset.get(i)
            if item is None:
                n += 1
                next_index += 1
            else:
                data.append(item)

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
            }
