"""List utility functions."""

__author__ = "730245854"


# TODO: Implement your functions here.
def main() -> None:
    """Results of functions."""
    group: list[int] = []
    print(all(group, 1))
    first: list[int] = [1, 1, 1, 1]
    second: list[int] = []
    print(is_equal(first, second))
    s: list[int] = [1, 1, 1, 1]
    print(max(s))


def all(xs: list[int], x: int) -> bool: 
    """Identify if list items are the same."""
    i: int = 0

    while i < len(xs): 
        if x != xs[i]:
            return False
        i += 1 
    return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """Identify if lists are the same."""
    i: int = 0

    while i < len(a):
        if a[i] != b[i]:
            return False
        if len(a) != len(b):
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Identify largest number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
  
    max = -9999999999999

    for val in input:
        if val > max:
            max = val

    return max


if __name__ == "__main__":
    main()
