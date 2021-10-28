"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730245854"


def test_invert_edge() -> None:
    """Test with empty list."""
    front: dict[str, str] = {}
    assert invert(front) == {}


def test_invert_use1() -> None:
    """Test with two entry pairs."""
    front: dict[str, str] = {"apples": "oranges", "mac": "cheese"}
    assert invert(front) == {"oranges": "apples", "cheese": "mac"}


def test_invert_use2() -> None:
    """Test with three entry pairs."""
    front: dict[str, str] = {"book": "movie", "lemons": "lemonade", "go": "heels"}
    assert invert(front) == {"movie": "book", "lemonade": "lemons", "heels": "go"}


def test_favorite_color_use1() -> None:
    """Test with two colors."""
    s: dict[str, str] = {"Sawyer": "green", "Dr. J": "red"}
    assert favorite_color(s) == "green"


def test_favorite_color_use2() -> None:
    """Test with a simple majority."""
    s: dict[str, str] = {"Sawyer": "green", "Dr. J": "red", "Josh": "green"}
    assert favorite_color(s) == "green"


def test_favorite_color_edge() -> None: 
    """Test with an empty list."""
    s: dict[str, str] = {}
    assert favorite_color(s) == ""


def test_count_use1() -> None:
    """Test with one list item."""
    unit: list[str] = ["guitar"]
    assert count(unit) == {"guitar": 1}


def test_count_use2() -> None:
    """Test with three list items."""
    unit: list[str] = ["guitar", "violin", "guitar"]
    assert count(unit) == {"guitar": 2, "violin": 1}


def test_count_empty() -> None:
    """Test with an empty list."""
    unit: list[str] = []
    assert count(unit) == {}