class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if self.data == value:
            return True
        elif value < self.data and self.left is not None:
            return self.left.find_char(value)
        elif value >= self.data and self.right is not None:
            return self.right.find_char(value)
        return False

    def sum(self):
        if self.left == None and self.right == None:
            return self.data
        total = 0
        total += self.left.sum() if self.left else 0
        total += self.right.sum() if self.right else 0
        total += self.data
        return total

    def print_preorder(self):
        print(self.data)
        if self.left: self.left.print_inorder()
        if self.right: self.right.print_inorder()

    def print_inorder(self):
        if self.left: self.left.print_preorder()
        print(self.data)
        if self.right: self.right.print_preorder()

    def print_postorder(self):
        if self.left: self.left.print_postorder()
        if self.right: self.right.print_postorder()
        print(self.data)

    def postorder_list(self):
        result = []
        if self.left:
            result += self.left.postorder_list()
        if self.right:
            result += self.right.postorder_list()
        return result + [self.data]


import unittest


class Tests(unittest.TestCase):
    def tests(self):
        btree = Node(10)
        btree.insert(2)
        btree.insert(30)
        btree.insert(1)
        self.assertTrue(btree.find(30))
        self.assertFalse(btree.find(44))

    def sum_tests(self):
        btree = Node(10)
        btree.insert(10)
        btree.insert(10)
        btree.insert(10)
        self.assertEqual(btree.sum(), 40)
        self.assertNotEqual(btree.sum(), 30)

    def test_preorder(self):
        btree = Node(10)
        btree.insert(2)
        btree.insert(4)
        btree.insert(30)
        btree.insert(1)
        btree.print_preorder()

    def test_inorder(self):
        btree = Node(10)
        btree.insert(2)
        btree.insert(4)
        btree.insert(30)
        btree.insert(1)
        btree.print_inorder()

    def test_postorder(self):
        btree = Node(10)
        btree.insert(2)
        btree.insert(4)
        btree.insert(30)
        btree.insert(1)
        btree.print_postorder()

    def test_postorder_list(self):
        btree = Node(10)
        btree.insert(2)
        btree.insert(4)
        btree.insert(30)
        btree.insert(1)
        self.assertListEqual([1, 4, 2, 30, 10], btree.postorder_list())
