#!/usr/bin/env python3
""" return tuple """


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return tuple """
    return (k, float(v)**2)
