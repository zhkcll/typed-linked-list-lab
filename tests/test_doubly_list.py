import unittest
from linked_list.doubly_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_append(self):
        dll = DoublyLinkedList[int]()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        self.assertEqual(str(dll), "1 <-> 2 <-> 3")
        self.assertEqual(len(dll), 3)

    def test_remove(self):
        dll = DoublyLinkedList[int]()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        dll.remove(2)
        self.assertEqual(str(dll), "1 <-> 3")
        self.assertEqual(len(dll), 2)

    def test_remove_nonexistent(self):
        dll = DoublyLinkedList[int]()
        dll.append(1)
        self.assertFalse(dll.remove(999))

if __name__ == "__main__":
    unittest.main()
