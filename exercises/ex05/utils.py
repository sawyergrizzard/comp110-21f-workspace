"""List utility functions part 2."""

__author__ = "730245854"


def only_evens(xs: list[int]) -> list[int]: 
    """Returns a list containing only even elements."""
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 != 0: 
            xs.pop(i)
        else: 
            i += 1
    return xs


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Returns list items between two indices."""
    i: list[int] = a_list
    if len(i) == 0:
        return []
    while end < len(i):
        if end <= 0:
            return []
        i.pop(end)
    while start > 0:
        if len(i) < start:
            return []
        i.pop(start - 1)
        start -= 1
    return i


def concat(a: list[int], b: list[int]) -> list[int]:
    """Combines two lists into one list.""" 
    while 0 < len(b):
        a.append(b[0])
        b.pop(0)
    return a


nums: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(only_evens(nums))
sub_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x: int = 25
y: int = -4
print(sub(sub_list, x, y))
first: list[int] = [3, 4, 5]
second: list[int] = [6, 7, 8]
print(concat(first, second))
