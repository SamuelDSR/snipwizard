from snipwizard.ds.doubly_linked_list import DoublyLinkedList


def test_append():
    dlist = DoublyLinkedList()
    dlist.append(100)
    assert (dlist.head is not None and dlist.tail is not None), \
        "head tail must not be none after first append"
    assert dlist.head == dlist.tail, "head must equal to tail after fist append"
    assert dlist.head.prev is None, "head prev must be none"
    assert dlist.tail.next is None, "tail next must be none"
    dlist.append(200)
    assert dlist.head.data == 100, "head data must be 100 after append 100,200"
    assert dlist.tail.data == 200, "tail data must be 200 after append 100,200"
    assert dlist.head.prev is None, "head prev must be none"
    assert dlist.tail.next is None, "tail next must be none"
    assert dlist.head.next == dlist.tail, "head next must be tail after append 100,200"
    assert dlist.tail.prev == dlist.head, "tail prev must be head after append 100,200"


def test_appendleft():
    dlist = DoublyLinkedList()
    dlist.appendleft(100)
    assert (dlist.head is not None and dlist.tail is not None), \
        "head tail must not be none after first appendleft"
    assert dlist.head == dlist.tail, "head must equal to tail after fist appendleft"
    assert dlist.head.prev is None, "head prev must be none"
    assert dlist.tail.next is None, "tail next must be none"
    dlist.appendleft(200)
    assert dlist.head.data == 200, "head data must be 200 after appendleft 100,200"
    assert dlist.tail.data == 100, "tail data must be 100 after appendleft 100,200"
    assert dlist.head.prev is None, "head prev must be none"
    assert dlist.tail.next is None, "tail next must be none"
    assert dlist.head.next == dlist.tail, "head next must be tail after append 100,200"
    assert dlist.tail.prev == dlist.head, "tail prev must be head after append 100,200"


def test_from_seq():
    dlist = DoublyLinkedList.from_seq([1, 2, 3, 4])
    assert dlist.head.prev is None, "head prev must be none"
    assert dlist.tail.next is None, "tail next must be none"
    assert dlist.head.data == 1, "head data must be 1 after from_seq(1,2,3,4)"
    assert dlist.tail.data == 4, "tail data must be 4 after from_seq(1,2,3,4)"
    assert dlist.head.next.data == 2, "head.next data must be 2 after from_seq(1,2,3,4)"
    assert dlist.tail.prev.data == 3, "tail.prev data must be 3 after from_seq(1,2,3,4)"


def test_remove():
    dlist = DoublyLinkedList()
    # 4 -> 2 -> 1 -> 3
    dlist.append(1)
    dlist.appendleft(2)
    dlist.append(3)
    dlist.appendleft(4)
    # remove 1
    dlist.remove(dlist.tail.prev)
    assert dlist.tail.prev.data == 2, "tail previous node must be 2 after removing 1"
    assert dlist.head.next.next == dlist.tail,\
        "head.next.next must equal to tail after removing 1"

    # remove 4
    dlist.remove(dlist.head)
    assert dlist.head.data == 2, "head must be 2 after removing 1, 4"
    assert dlist.head.next.data == 3, "head.next.data must be 3 after removing 1, 4"

    # remove 3
    dlist.remove(dlist.tail)
    assert dlist.tail.data == 2, "tail must be 2 after removing 1, 4, 3"
    assert dlist.head == dlist.tail, "head must equal to tail after removing 1, 4, 3"
    assert dlist.head.prev is None, "head prev must be none"
    assert dlist.tail.next is None, "tail next must be none"


def test_insert_after():
    dlist = DoublyLinkedList.from_seq([1, 2, 3, 4])
    dlist.insert_after(dlist.head, 5)
    assert dlist.head.next.data == 5, "head next must be 5 after insert_after 5 to head"
    assert [n.data for n in dlist.traverse()] == [1, 5, 2, 3, 4],\
        "List traverse must be [1, 5, 2, 3, 4] after insert_after to head"
    assert [n.data for n in dlist.traverse(True)] == [4, 3, 2, 5, 1],\
        "List traverse must be [4, 3, 2, 5, 1] after insert_after to head"
