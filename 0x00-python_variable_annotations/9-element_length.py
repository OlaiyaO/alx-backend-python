#!/usr/bin/env python3
'''Module for Task 9.
'''
from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Calculates the length of each sequence in a list of sequences.
    '''
    return [(item, len(item)) for item in lst]
