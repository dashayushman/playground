class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        if not self.next:
            self.next = Node(value)
        else:
            self.next.add(value)

    def add_iter(self, value):
        prev = None
        node = self
        while node:
            prev = node
            node = node.next
        prev.next = Node(value)

    def traverse(self):
        results = []
        node = self
        while node:
            results.append(node.value)
            node = node.next
        return results

ll = Node(1)

ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)

ll.add_iter(5)

import unittest


class Tester(unittest.TestCase):
    def tests(self):
        self.assertEqual([1, 2, 3, 4, 5, 5], ll.traverse())
