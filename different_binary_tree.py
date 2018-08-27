import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value else None

    def _insert_value(self, node, value):
        if value >= node.value:
            if node.right:
                self._insert_value(node.right, value)
            else:
                node.right = Node(value)
        else:
            if node.left:
                self._insert_value(node.left, value)
            else:
                node.left = Node(value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_value(self.root, value)

    def insert_list(self, values):
        for value in values:
            self.insert(value)

    def _find_value(self, node, value, level):
        found, found_level = False, -1
        if node:
            if node.value == value:
                found, found_level = True, level
            elif value >= node.value:
                found, found_level = self._find_value(node.right, value, level + 1)
            else:
                found, found_level = self._find_value(node.left, value, level + 1)
        return found, found_level

    def find(self, value):
        return self._find_value(self.root, value, level=0)

    def find_level(self, value):
        return self.find(value)[-1]

    def find_value(self, value):
        return self.find(value)[0]

    def _find_height(self, node):
        if not node: return 0
        return max(self._find_height(node.left),
                      self._find_height(node.right)) + 1

    def height(self):
        return self._find_height(self.root) -1

    def _values_at_level(self, node, level, results):
        if node:
            if level == 0:
                results.append(node.value)
            else:
                self._values_at_level(node.left, level-1, results)
                self._values_at_level(node.right, level - 1, results)
        return results

    def values_at_level(self, level):
        return self._values_at_level(self.root, level, [])


    def _preorder(self, node, result):
        if not node: return result
        result.append(node.value)
        self._preorder(node.left, result)
        self._preorder(node.right, result)
        return result

    def _inorder(self, node, result):
        if not node: return result
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)
        return result

    def _postorder(self, node, result):
        if not node: return result
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.value)
        return result

    def _bfs(self):
        height = self.height()
        bfs_results = []
        for h in range(height + 1):
            bfs_results += self.values_at_level(h)
        return bfs_results

    def _alternative_bfs(self):
        q = []
        if self.root: q.append(self.root)
        results = []
        while q:
            results.append(q[0].value)
            if q[0].left: q.append(q[0].left)
            if q[0].right: q.append(q[0].right)
            q.pop(0)
        return results



    def tolist(self, mode='PREORDER'):
        result = []
        if mode == 'PREORDER':
            return self._preorder(self.root, result)
        elif mode == 'INORDER':
            return self._inorder(self.root, result)
        elif mode == 'POSTORDER':
            return self._postorder(self.root, result)
        elif mode == 'BFS':
            return self._alternative_bfs()
        else:
            raise NotImplementedError('{} has not been implemented yet or is '
                              'an invalid traversal strategy'.format(mode))


class Tester(unittest.TestCase):
    def test_btree_insert(self):
        btree = BinaryTree()
        btree.insert(10)
        btree.insert(20)
        btree.insert(1)
        btree.insert(8)

        self.assertTupleEqual(btree.find(8), (True, 2))
        self.assertTupleEqual(btree.find(99), (False, -1))

        self.assertEqual(btree.find_level(8), 2)
        self.assertEqual(btree.find_level(20), 1)
        self.assertEqual(btree.find_level(10), 0)
        self.assertEqual(btree.find_level(900), -1)


        self.assertListEqual(btree.tolist(mode='PREORDER'), [10, 1, 8, 20])
        self.assertListEqual(btree.tolist(mode='INORDER'), [1, 8, 10, 20])
        self.assertListEqual(btree.tolist(mode='POSTORDER'), [8, 1, 20, 10])
        self.assertListEqual(btree.tolist(mode='BFS'), [10, 1, 20, 8])
        with self.assertRaises(NotImplementedError):
            btree.tolist(mode='BLAH')

    def test_height(self):
        btree = BinaryTree()
        btree.insert_list([10, 23, -1, 45, 89, 2, 0, 3])

        self.assertEqual(btree.height(), 3)
        self.assertListEqual(btree.values_at_level(level=6), [])
        self.assertListEqual(btree.values_at_level(level=0), [10])
        self.assertListEqual(btree.values_at_level(level=1), [-1, 23])
        self.assertListEqual(btree.values_at_level(level=2), [2, 45])
        self.assertListEqual(btree.values_at_level(level=3), [0, 3, 89])
