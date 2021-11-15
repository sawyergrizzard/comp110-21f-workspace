"""Examples of optional parameters and Union type parameters."""


def hello(name: str = "World") -> str:
    """A delightful greeting function."""
    result: str = "Hello, "
    return result + name


# Calling hello with no arguments leads to use of default value
print(hello())
# Calling hello with one argument overrides the default value
print(hello("Ezekiel"))
print(hello(110))