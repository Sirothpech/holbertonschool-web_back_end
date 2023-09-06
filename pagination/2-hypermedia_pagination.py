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

    def get_page(self, page=1, page_size=10):
        # Vérifier que page et page_size sont des entiers positifs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Récupérer les données
        data = self.dataset()

        # Utiliser index_range pour obtenir les indices de début et de fin
        start_index, end_index = index_range(page, page_size)

        # Extraire la page de données
        page_data = data[start_index:end_index]

        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        # Vérifier que page et page_size sont des entiers positifs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculer les index de début et de fin pour la pagination
        start, end = index_range(page, page_size)
        dataset = self.dataset()

        # Calculer le nombre total de pages dans le dataset
        total_pages = math.ceil(len(dataset) / page_size)

        # Si la pagination commence après la fin du dataset,
        # retourner une page vide
        if start >= len(dataset):
            return {
                'page_size': page_size,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': total_pages
            }

        # Extraire les données de la page actuelle
        data = dataset[start:end]

        # Calculer les numéros de page précédente et suivante
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        # Créer un dictionnaire contenant les informations de pagination
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
