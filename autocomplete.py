import unittest


class Node:
    def __init__(self):
        self.vocab = {}
        self.end = False

    @property
    def is_end(self):
        return self.end

    def get_vocab_keys(self):
        return self.vocab.keys()

    def vocab_contains(self, char):
        return char in self.vocab

    def get_char_node(self, char):
        return self.vocab[char]

    def insert(self, char, end):
        self.vocab[char] = Node()
        self.vocab[char].end = end


class AutoCompleter:
    def __init__(self, corpus):
        self.root = Node()
        for token in corpus:
            self.insert(self.root, token)

    def insert(self, node, string):
        if not string: return
        end = len(string) == 1
        if node.vocab_contains(string[0]):
            if end:
                node.vocab[string[0]].end = end
            self.insert(node.vocab[string[0]], string[1:])
        else:
            node.insert(string[0], end)
            self.insert(node.vocab[string[0]], string[1:])

    def _find_char(self, node, char):
        if node.vocab_contains(char): return True
        found = False
        for c in node.get_vocab_keys():
            found = self._find_char(node.get_char_node(c), char)
            if found:
                break
        return found

    def find_char(self, char):
        return self._find_char(self.root, char)

    def _find(self, node, token):
        if not token:
            if node.is_end:
                return True
            else:
                return False
        if node.vocab_contains(token[0]):
            return self._find(node.get_char_node(token[0]), token[1:])
        else:
            return False

    def find(self, token):
        return self._find(self.root, token)

    def _exec_complete(self, node, stack, results):
        if node.is_end:
            results.append("".join(stack))
        if not node.get_vocab_keys(): return results
        for c_i, c in enumerate(node.get_vocab_keys()):
            stack.append(c)
            self._exec_complete(node.get_char_node(c), stack, results)
            stack.pop()
        return results

    def complete(self, prefix):
        stack = []
        results = []
        node = self.root
        for c in prefix:
            if node.vocab_contains(c):
                stack.append(c)
                node = node.get_char_node(c)
            else:
                return results
        return self._exec_complete(node, stack, results)


class Tester(unittest.TestCase):
    def test_autocomplete(self):
        ac = AutoCompleter(["deer", "door", "do", "dog", "cat", "cabbage", "cabbie"])

        self.assertTrue(ac.find_char('d'))
        self.assertTrue(ac.find_char('o'))
        self.assertTrue(ac.find_char('i'))
        self.assertFalse(ac.find_char('z'))

        self.assertTrue(ac.find('dog'))
        self.assertTrue(ac.find('deer'))
        self.assertTrue(ac.find('cabbage'))
        self.assertFalse(ac.find('blah'))

        d_suggestions = ac.complete("d")
        print(d_suggestions)
        for target in ["deer", "door", "dog", "do"]:
            self.assertTrue(target in d_suggestions)

        c_suggestions = ac.complete("c")
        for target in ["cat", "cabbage", "cabbie"]:
            self.assertTrue(target in c_suggestions)

        cab_suggestions = ac.complete("cab")
        for target in ["cabbage", "cabbie"]:
            self.assertTrue(target in cab_suggestions)
