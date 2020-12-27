from __future__ import annotations
from typing import Any, Iterator, Optional, Sequence

from snipwizard.ds.doubly_linked_list import Node


class CircularDoublyLinkedList:
    """Circular Doubly Linked List with two pointers: head and tail.
    If there is only one node, then node.next == node, node.prev == node
    """
    def __init__(self) -> None:
        self.first_node = None

    def insert_after(self, prev_node: Optional[Node], data: Any) -> Node:
        if prev_node is None:
            raise ValueError("Given previous node cannot be null")
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        new_node.next.prev = new_node
        return new_node

    @classmethod
    def from_seq(cls, seq: Sequence[Any]) -> CircularDoublyLinkedList:
        dlist = CircularDoublyLinkedList()
        prev_node = None
        for item in seq:
            if prev_node is None:
                prev_node = Node(item)
                prev_node.next = prev_node
                prev_node.prev = prev_node
                dlist.first_node = prev_node
            else:
                prev_node = dlist.insert_after(prev_node, item)
        return dlist

    def traverse(self, first_node: Optional[Node] = None, include_first:bool = True) -> Iterator[Node]:
        """Traverse the list from a given first_node
        If first_node is not given (None), use the first_node as default.
        If the given node is not in list, raise Error
        """
        if first_node is None:
            first_node = self.first_node
        # list is empty
        if first_node is None:
            return
        # start from first_node of <list>, find the given first_node
        current_node = self.first_node
        while current_node != first_node:
            current_node = current_node.next
            # a cycle must have been traverse
            if current_node == self.first_node:
                break

        # given first_node not in list
        if current_node != first_node:
            raise ValueError("Given first_node is not in list")

        if include_first:
            yield first_node

        current_node = first_node.next
        while current_node != first_node and current_node is not None:
            yield current_node
            current_node = current_node.next

    def remove(self, node: Optional[Node]) -> None:
        if node is None:
            raise ValueError("The node to remove cannot be null")
        prev, next = node.prev, node.next
        # Must have only one node
        if prev == next and prev == node:
            self.first_node = None
        # Must have two nodes
        elif prev == next:
            prev.next = prev
            prev.prev = prev
            self.first_node = prev
        else:
            prev.next = next
            next.prev = prev
            # check if the removed node is self.first_node
            if node == self.first_node:
                self.first_node = next
        # GC efficiency
        node.prev, node.next = None, None
