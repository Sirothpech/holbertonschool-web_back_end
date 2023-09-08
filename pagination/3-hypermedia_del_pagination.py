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
        """Return a hypermedia page based on index and page_size."""
        # Check if index is in a valid range
        assert index is None or (isinstance(index, int) and index >= 0)

        # Get the indexed dataset
        indexed_data = self.indexed_dataset()

        # Determine the current index
        if index is None:
            current_index = 0
        else:
            current_index = index

        # Calculate the next index
        next_index = current_index + page_size

        # Get the current page data
        page_data = [indexed_data[i]
                     for i in range(current_index, next_index)
                     if i in indexed_data]

        # Calculate the total number of pages
        total_pages = math.ceil(len(indexed_data) / page_size)

        # Create the hypermedia page dictionary
        hypermedia_page = {
            "index": current_index,
            "next_index": next_index
            if next_index < len(indexed_data) else None,
            "page_size": page_size,
            "data": page_data,
            "total_pages": total_pages
        }

        return hypermedia_page
