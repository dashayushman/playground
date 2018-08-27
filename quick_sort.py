import unittest


def quicksort(data):
    less = []
    more = []
    pivot_list = []

    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        for val in data:
            if val < pivot:
                less.append(val)
            elif val > pivot:
                more.append(val)
            else:
                pivot_list.append(val)

        less = quicksort(less)
        more = quicksort(more)
        return less + pivot_list + more


class Tests(unittest.TestCase):
    def test_quicksort(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5], quicksort([5, 4, 3, 2, 1, 0]))
        self.assertListEqual([-11, 42, 132, 4567], quicksort([42, -11, 4567, 132]))
        self.assertListEqual([], quicksort([]))
