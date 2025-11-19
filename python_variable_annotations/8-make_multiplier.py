#!/usr/bin/env python3
"""This module is for a project."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(value: float) -> float:
        """Multiply a float by a multiplier."""
        return value * multiplier
    return multiply
