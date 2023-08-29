#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return
values with the appropriate types
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains a sequence
    from the input list and its corresponding length.

    Args:
        lst (Iterable[Sequence]): A list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
        contains a sequence from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
