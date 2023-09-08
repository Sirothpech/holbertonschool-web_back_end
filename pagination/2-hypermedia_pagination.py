#!/usr/bin/env python3
"""
Hypermedia pagination
"""


import csv
from typing import List, Dict
import math


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The file path of the dataset containing
        popular baby names.

    Methods:
        dataset() -> List[List]: Returns the cached dataset of baby names.
        get_page(page: int = 1, page_size: int = 10) -> List[List]: Retrieves
        a specific page of data from the dataset based
        on the given page number and page size.
        get_hyper(page: int = 1, page_size: int = 10) -> Dict: Retrieves
        a specific page of data from the dataset based on the given page
        number and page size, along with pagination information.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset of baby names.

        Returns:
            List[List]: The dataset of baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset based on
        the given page number and page size.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of records per page.
            Defaults to 10.

        Returns:
            List[List]: The data of the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        start_index, end_index = index_range(page, page_size)

        page_data = data[start_index:end_index]

        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves a specific page of data from the dataset based on the given
        page number and page size, along with pagination information.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of records per page.
            Defaults to 10.

        Returns:
            Dict: A dictionary containing the page data and
            pagination information.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        total_pages = math.ceil(len(dataset) / page_size)

        if start >= len(dataset):
            return {
                'page_size': page_size,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': total_pages
            }

        data = dataset[start:end]

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
