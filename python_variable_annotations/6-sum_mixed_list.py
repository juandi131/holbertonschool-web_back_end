#!/usr/bin/env python3
""" takes a list mxd_lst of integers and floats and returns float """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list mxd_lst of integers and floats and returns float """
    result = 0.0
    for num in mxd_lst:
        result += num
    return float(result)
