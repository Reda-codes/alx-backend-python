#!/usr/bin/env python3
'''
type-annotated function sum_mixed_list
'''
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[float, int]]) -> float:
    '''sum mixed'''
    return sum(mxd_lst)
