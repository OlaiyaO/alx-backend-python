#!/usr/bin/env python3
'''Module for Task 8.
'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Generates a function that multiplies its input by
    the given multiplier.
    '''
    return lambda x: x * multiplier
