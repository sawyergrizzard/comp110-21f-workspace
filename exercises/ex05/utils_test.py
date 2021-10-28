"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730245854"


def test_only_evens_empty() -> None:
    """Test with empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_two() -> None:
    """Test with one even number."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_odds() -> None:
    """Test with only odd numbers."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_sub_use1() -> None:
    """Test with increasing numbers."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [2, 3]


def test_sub_use2() -> None:
    """Test with decreasing numbers."""
    a_list: list[int] = [10, 9, 8, 7, 6]
    start: int = 2
    end: int = 4
    assert sub(a_list, start, end) == [8, 7]


def test_sub_edge() -> None: 
    """Test with a negative end index."""
    a_list: list[int] = [6, 7, 8, 9, 10]
    start: int = 2
    end: int = -4
    assert sub(a_list, start, end) == []


def test_concat_empty() -> None:
    """Test with an empty list."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_use1() -> None:
    """Test with two identical lists."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [1, 2, 3]
    assert concat(a, b) == [1, 2, 3, 1, 2, 3]


def test_concat_use2() -> None:
    """Test with two basic lists."""
    a: list[int] = [5, 10]
    b: list[int] = [15, 20]
    assert concat(a, b) == [5, 10, 15, 20]
