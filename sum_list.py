import unittest


def is_sum_in_list(l, k):
    sum_in_list = False
    if not l: return sum_in_list
    memory = {}
    for val in l:
        diff = val - k
        if diff in memory:
            sum_in_list = True
            break
        else:
            memory[val] = None
    return sum_in_list


class Tests(unittest.TestCase):
    def test(self):
        self.assertTrue(is_sum_in_list([0, 10, 22, 100], 10), True)
        self.assertFalse(is_sum_in_list([0, 10, 22, 100], 554), False)
        self.assertFalse(is_sum_in_list([0, 10, -2, 100], 8), True)
        self.assertFalse(is_sum_in_list([0, -10, -2, 100], -12), True)
        self.assertFalse(is_sum_in_list([], -12), False)
