#!/usr/bin/env python3
"""Contains a function to sum a list of mixed integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up a list of mixed integers and floats."""
    return sum(mxd_lst)
