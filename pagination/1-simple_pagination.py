#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


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
        DATA_FILE (str): The filename of the CSV file containing the dataset
        of popular baby names.

    Methods:
        __init__(): Initializes the Server class.
        dataset() -> List[List]: Returns the cached dataset.
        get_page(page: int = 1, page_size: int = 10) -> List[List]: Retrieves
        a specific page of data from the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server class.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset.

        Returns:
            List[List]: The cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve. Default is 1.
            page_size (int): The number of records per page. Default is 10.

        Returns:
            List[List]: The data for the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        start_index, end_index = index_range(page, page_size)

        page_data = data[start_index:end_index]

        return page_data
