#!/usr/bin/env python3
""" simple helper """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ index range """
    tup: int = page_size * page - page_size
    return (tup, page_size * page)
