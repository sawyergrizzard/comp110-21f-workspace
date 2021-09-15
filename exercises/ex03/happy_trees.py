"""Drawing forests in a loop."""

__author__ = "730245854"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
amount: int = int(input("Depth: "))
i = 1 

while i <= amount:
    print((TREE) * i)
    i = i + 1 
