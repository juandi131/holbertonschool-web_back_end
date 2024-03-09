#!/usr/bin/env python3
""" takes a list of floats returns the sum """


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes a list of floats returns the sum """
    result = 0.0
    for num in input_list:
        result += num
    return float(result)
