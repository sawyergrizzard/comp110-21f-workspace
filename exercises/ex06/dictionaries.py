"""Practice with dictionaries."""

__author__ = "730245854"

# Define your functions below


def invert(front: dict[str, str]) -> dict[str, str]:
    """Returns an inverted dictionary."""
    back = {}
    for key, value in front.items():
        back = {value: key for key, value in front.items()}
        if value in back and value in front:
            raise KeyError("No duplicate keys!")
    return back


def favorite_color(s: dict[str, str]) -> str:
    """Returns the most common color."""
    favorite: str = ""
    dicts: dict[str, int] = {}
    max: int = 0
    for item in s:
        if item not in dicts:
            dicts[s[item]] = 1
        else:
            dicts[s[item]] += 1
    for item in dicts:
        if dicts[item] > max:
            favorite = item
            max = dicts[favorite]
    return favorite


def count(unit: list[str]) -> dict[str, int]:
    """Counts number of times each value appears in a list."""
    counted: dict[str, int] = {}
    for item in unit:
        if item not in counted:
            counted[item] = 1
        else:
            counted[item] += 1
    return counted


items = {"one": "two", "three": "four", "five": "six"}
print(invert(items))
colors = {"Sawyer": "blue", "Josh": "green", "Matt Amodio": "green", "Colby": "blue", "Dr. J": "green"}
print(favorite_color(colors))
objects: list[str] = ["hat", "shirt", "pants"]
print(count(objects))
