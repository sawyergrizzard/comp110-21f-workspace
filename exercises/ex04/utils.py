"""List utility functions."""

__author__ = "730245854"


# TODO: Implement your functions here.
def main() -> None:
    group: list[int] = [1, 1, 1, 1, 1, 1, 1, 1]
    print(all(group, 1))
    first: list[int] = [1, 1, 1, 1]
    second: list[int] = [1, 1, 1, 1, 1, 1, 1]
    print(is_equal(first, second))
    s: list[int] = [1, 1, 1, 1]
    print(max(s))


def all(xs: list[int], x: int) -> bool: 
    i: int = 0

    while i < len(xs): 
        if x != xs[i]:
            return False
        i += 1 
    return True


def is_equal(a: list[int], b: list[int]) -> bool:
    i: int = 0

    while i < len(a):
        if a[i] != b[i]:
            return False
        if len(a) != len(b):
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    #  z: int = 0
    #  y: int = len(input) - 1

    max = -9999999999999

    for val in input:
        if val > max:
            max = val

    # while len(input) > 1:
    #     if input[z] > input[y]: 
    #         input.pop(input[y])
    #     if input[z] <= input[y]:
    #         input.pop(input[z])
    # return input[z]

    return max


if __name__ == "__main__":
    main()