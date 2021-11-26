"""Simple linked list example."""

from __future__ import annotations

from typing import Optional


class Node:
    """Single linked list Node."""
    data: int
    next: Optional[Node] 

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor."""
        self.data = data
        self.next = next


third_node: Node = Node(3, None)
second_node: Node = Node(2, third_node)
a_node: Node = Node(1, second_node)
print(a_node.data.next)