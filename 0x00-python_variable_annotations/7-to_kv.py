#!/usr/bin/env python3
'''
type-annotated function to_kv
'''
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    '''to_kv function'''
    return (k, v ** 2)
