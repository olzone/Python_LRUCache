import unittest
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def test_head(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.getHead(), None)
        dll.addDataToList("data")
        self.assertEqual(dll.getHead().getData(), "data")
        dll.addDataToList("data2")
        self.assertEqual(dll.getHead().getData(), "data2")

    def test_tail(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.getTail(), None)
        dll.addDataToList("data")
        self.assertEqual(dll.getTail().getData(), "data")
        dll.addDataToList("data2")
        self.assertEqual(dll.getTail().getData(), "data")

    def test_size(self):
        dll = DoublyLinkedList()
        self.assertEqual(dll.getSize(), 0)
        dll.addDataToList("data")
        self.assertEqual(dll.getSize(), 1)
        dll.addDataToList("data2")
        self.assertEqual(dll.getSize(), 2)
        dll.removeTail()
        self.assertEqual(dll.getSize(), 1)
        dll.removeTail()
        self.assertEqual(dll.getSize(), 0)

    def test_moveToHead(self):
        dll = DoublyLinkedList()
        n1 = dll.addDataToList("data1")
        n2 = dll.addDataToList("data2")
        n3 = dll.addDataToList("data3")
        self.assertEqual(dll.toList(), ["data3", "data2", "data1"])

        dll.moveNodeToHead(n1) #move tail to head
        self.assertEqual(dll.toList(), ["data1", "data3", "data2"])

        dll.moveNodeToHead(n3)  # move node inside list
        self.assertEqual(dll.toList(), ["data3", "data1", "data2"])

        dll.moveNodeToHead(n3)  # move head to head
        self.assertEqual(dll.toList(), ["data3", "data1", "data2"])


if __name__ == '__main__':
    unittest.main()