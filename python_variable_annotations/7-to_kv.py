#!/usr/bin/env python3
"""This module is for a project."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square of v."""
    return (k, float(v * v))
