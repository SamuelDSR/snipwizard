import pytest
from snipwizard.ds.circular_doubly_linked_list import CircularDoublyLinkedList
from snipwizard.ds.doubly_linked_list import Node

def test_from_seq():
    cdlist = CircularDoublyLinkedList.from_seq([1,2,3,4])
    assert cdlist.first_node.data == 1, "first node must be 1 after from_seq(1,2,3,4)"
    assert cdlist.first_node.prev.data == 4, "prev of first node must be 4 after from_seq(1,2,3,4)"


def test_traverse():
    cdlist = CircularDoublyLinkedList.from_seq([1,2,3,4])
    first_node = cdlist.first_node.next
    assert [n.data for n in cdlist.traverse(first_node)] == [2, 3, 4, 1]

    cdlist = CircularDoublyLinkedList()
    assert len([n.data for n in cdlist.traverse(cdlist.first_node)]) == 0

    cdlist = CircularDoublyLinkedList.from_seq([10, 20])
    with pytest.raises(ValueError):
        [n.data for n in cdlist.traverse(Node(100))]


def test_insert_after():
    cdlist = CircularDoublyLinkedList.from_seq([2])
    node = cdlist.insert_after(cdlist.first_node, 3)
    node = cdlist.insert_after(node.prev, 4)
    # 2 -> 4 -> 3
    assert [n.data for n in cdlist.traverse(node)] == [4, 3, 2]


def test_remove():
    cdlist = CircularDoublyLinkedList.from_seq([2, 3, 4, 7])
    node = cdlist.first_node.prev
    cdlist.remove(node)
    assert [n.data for n in cdlist.traverse()] == [2, 3, 4]
