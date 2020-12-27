from __future__ import annotations
from typing import Any, Iterator, Optional, Sequence


class Node:
    def __init__(self, data: Any,
                 next: Optional[Node] = None,
                 prev: Optional[Node] = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "Node data: {}".format(self.data)

    def __str__(self):
        return repr(self)


class DoublyLinkedList:
    """Doubly Linked List with two pointers: head and tail
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def appendleft(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove(self, node: Optional[Node]) -> None:
        """Remove a node from list.
        Mote: this method assumes that node must in list
        """
        if node is None:
            raise ValueError("The node to remove cannot be null")
        prev, next = node.prev, node.next
        # node is head
        if prev is None:
            next.prev = None
            self.head = next
        # node is tail
        elif next is None:
            prev.next = None
            self.tail = prev
        else:
            prev.next = next
            next.prev = prev
        # GC efficiency
        node.next, node.prev = None, None

    @classmethod
    def from_seq(cls, seq: Sequence[Any]) -> DoublyLinkedList:
        dlist = DoublyLinkedList()
        for data in seq:
            dlist.append(data)
        return dlist

    def traverse(self, reversed: bool = False) -> Iterator[Node]:
        node = self.head if not reversed else self.tail
        while node is not None:
            yield node
            node = node.next if not reversed else node.prev

    def insert_after(self, prev_node: Optional[Node], data: Any) -> Node:
        """Insert a node after prev_node
        NOTE: this assumes that prev_node must in list
        """
        if prev_node is None:
            raise ValueError("Given previous node cannot be null")
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        if prev_node == self.tail:
            self.tail = new_node
        return new_node

    def __repr__(self):
        return " -> ".join([str(n.data) for n in self.traverse()])

    def __str__(self):
        return repr(self)
