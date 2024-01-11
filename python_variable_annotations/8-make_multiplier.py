#!/usr/bin/env python3
""" return tuple """


from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return tuple """
    def mult(n: float) -> float:
        """ mult float """
        return n * multiplier
    return mult
