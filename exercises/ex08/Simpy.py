"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730245854"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a new Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """String representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill our values array by mutating object called on."""
        # Start with an empty values list
        self.values = []
        # Loop for 'times' number of times
        i: int = 0
        while i < times:
        #   append value parameter to the values array
            self.values.append
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        # Start an empty values list
        self.values = []
        # Be sure step is not 0.0 by asserting
        assert step != 0.0
        # When step is positive:
        if step > 0.0:
            # Initialize next value to start
            next_value: float = start 
            # While next value is less than stop value
            while next_value < stop: 
                # Add next value to values list
                self.values.append(next_value)
                # Update next value by adding the step to it
                next_value += step