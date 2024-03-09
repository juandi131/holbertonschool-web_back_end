#!/usr/bin/env python3
""" simple helper """
from typing import Tuple

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(iself, page: int, page_size: int) -> Tuple:
        """ index range """
        tup: int = page_size * page - page_size
        return (tup, page_size * page)

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
        """ get page """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        with open(self.DATA_FILE, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            start, end = self.index_range(page, page_size)
            page_data = data[start+1:end+1]
            return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get hyper """
        pag = self.get_page(page, page_size)
        with open(self.DATA_FILE, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        leng = len(self.dataset())
        rang = self.index_range(page, page_size)
        if rang[1] > leng:
            next_page = None
        else:
            next_page = page + 1
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        myDict = {
            'page_size': len(pag),
            'page': page,
            'data': pag,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(leng / page_size)
        }
        return myDict
