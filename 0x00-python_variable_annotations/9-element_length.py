#!/usr/bin/env python3
"""
Annotate the below function’s parameters
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length function
    """
    return [(x, len(x)) for x in lst]
