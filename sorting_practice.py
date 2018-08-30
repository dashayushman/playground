import unittest


def quicksort(data, reverse=False, key=None):
    less = []
    more = []
    pivot_l = []

    if len(data) <= 1:
        return data
    else:
        pivot = key(data[0]) if key else data[0]
        for d in data:
            compare_val = key(d) if key else d
            if compare_val < pivot:
                less.append(d)
            elif compare_val > pivot:
                more.append(d)
            else:
                pivot_l.append(d)

        less = quicksort(less, reverse, key)
        more = quicksort(more, reverse, key)
        return more + pivot_l+ less if reverse else less + pivot_l + more


def merge(left, right, reverse=False, key=None):
    merged = []
    if reverse:
        condition = lambda x, y: x > y
    else:
        condition = lambda x, y: x < y
    while left and right:
        l, r = (key(left[0]), key(right[0])) if key else (left[0], right[0])
        if condition(l, r):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    if left:
        merged += left
    if right:
        merged += right
    return merged


def mergesort(data, reverse=False, key=None):
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = mergesort(data[:middle], reverse, key)
    right = mergesort(data[middle:], reverse, key)
    return merge(left, right, reverse, key)


def insertionsort(data, reverse=False, key=None):
    condition = (lambda x, y: x < y) if reverse else (lambda x, y: x > y)
    for current_index in range(1, len(data)):
        current_data = data[current_index]
        current_value = key(data[current_index]) if key else data[current_index]
        position = current_index
        previous_value = key(data[position - 1]) if key else data[position - 1]
        while position > 0 and condition(previous_value, current_value):
            data[position] = data[position - 1]
            position = position -1
            previous_value = key(data[position]) if key else data[position]
        data[position] = current_data
    return data


def bubblesort(data, reverse=False, key=None):
    condition = (lambda x, y: x < y) if reverse else (lambda x, y: x > y)
    index = len(data) - 1
    while index >= 0:
        for j in range(index):
            value_1 = key(data[j]) if key else data[j]
            value_2 = key(data[j + 1]) if key else data[j + 1]
            if condition(value_1, value_2):
                data[j], data[j + 1] = data[j + 1], data[j]
        index -= 1
    return data


def heapify(data, heap_size, i, reverse=False, key=None):
    condition = (lambda x, y: x < y) if reverse else (lambda x, y: x > y)
    left = 2 * i + 1
    right = 2 * i + 2
    root = i

    if left < heap_size:
        left_val = key(data[left]) if key else data[left]
        root_val = key(data[root]) if key else data[root]
        if condition(left_val, root_val):
            root = left
    if right < heap_size:
        right_val = key(data[right]) if key else data[right]
        root_val = key(data[root]) if key else data[root]
        if condition(right_val, root_val):
            root = right
    if root != i:
        data[i], data[root]= data[root], data[i]
        heapify(data, heap_size, root, reverse, key)


def build_heap(data, reverse=False, key=None):
    heap_size = len(data)
    for i in range(heap_size // 2, -1, -1):
        heapify(data, heap_size, i, reverse, key)


def heapsort(data, reverse=False, key=None):
    heapsize = len(data)
    build_heap(data, reverse, key)
    for i in range(heapsize - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapsize -= 1
        heapify(data, heapsize, 0, reverse, key)
    return data


class SortingTests(unittest.TestCase):
    def test_quick_sort(self):
        
        self.assertListEqual([-1, 2, 45, 110], quicksort([-1, 45, 2, 110], reverse=False))
        self.assertListEqual([-1, 2, 44, 45, 110], quicksort([-1, 45, 2, 110, 44], reverse=False))
        self.assertListEqual(list(reversed([-1, 2, 45, 110])), quicksort([-1, 2, 45, 110], reverse=True))
        self.assertListEqual([], quicksort([]))
        self.assertListEqual(list(range(2, 100)), quicksort(list(range(99, 1, -1))))
        self.assertListEqual([(-24, 356), (-1, -24), (1, 20), (45, 100)],
                             quicksort([(1, 20), (45, 100), (-1, -24), (-24, 356)], key=lambda x: x[0]))
        self.assertListEqual([(-1, -24), (1, 20), (45, 100), (-24, 356)],
                             quicksort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=False, key=lambda x: x[1]))
        self.assertListEqual(list(reversed([(-1, -24), (1, 20), (45, 100), (-24, 356)])),
                             quicksort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=True, key=lambda x: x[1]))

    def test_mergesort(self):
        self.assertListEqual([-1, 2, 45, 110], mergesort([-1, 45, 2, 110], reverse=False))
        self.assertListEqual(list(reversed([-1, 2, 45, 110])), mergesort([-1, 2, 45, 110], reverse=True))
        self.assertListEqual([], mergesort([]))
        self.assertListEqual(list(range(2, 100)), mergesort(list(range(99, 1, -1))))
        self.assertListEqual([(-24, 356), (-1, -24), (1, 20), (45, 100)],
                             mergesort([(1, 20), (45, 100), (-1, -24), (-24, 356)], key=lambda x: x[0]))
        self.assertListEqual([(-1, -24), (1, 20), (45, 100), (-24, 356)],
                             mergesort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=False, key=lambda x: x[1]))
        self.assertListEqual(list(reversed([(-1, -24), (1, 20), (45, 100), (-24, 356)])),
                             mergesort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=True, key=lambda x: x[1]))

    def test_insertion(self):
        self.assertListEqual([-1, 2, 45, 110], insertionsort([-1, 2, 45, 110], reverse=False))
        self.assertListEqual(list(reversed([-1, 2, 45, 110])), insertionsort([-1, 2, 45, 110], reverse=True))
        self.assertListEqual([], insertionsort([]))
        self.assertListEqual(list(range(2, 100)), insertionsort(list(range(99, 1, -1))))
        self.assertListEqual([(-24, 356), (-1, -24), (1, 20), (45, 100)],
                             insertionsort([(1, 20), (45, 100), (-1, -24), (-24, 356)], key=lambda x: x[0]))
        self.assertListEqual([(-1, -24), (1, 20), (45, 100), (-24, 356)],
                             insertionsort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=False, key=lambda x: x[1]))
        self.assertListEqual(list(reversed([(-1, -24), (1, 20), (45, 100), (-24, 356)])),
                             insertionsort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=True, key=lambda x: x[1]))

    def test_bubblesort(self):
        self.assertListEqual([-1, 2, 45, 110], bubblesort([-1, 2, 45, 110], reverse=False))
        self.assertListEqual(list(reversed([-1, 2, 45, 110])), bubblesort([-1, 2, 45, 110], reverse=True))
        self.assertListEqual([], bubblesort([]))
        self.assertListEqual(list(range(2, 100)), bubblesort(list(range(99, 1, -1))))
        self.assertListEqual([(-24, 356), (-1, -24), (1, 20), (45, 100)],
                             bubblesort([(1, 20), (45, 100), (-1, -24), (-24, 356)], key=lambda x: x[0]))
        self.assertListEqual([(-1, -24), (1, 20), (45, 100), (-24, 356)],
                             bubblesort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=False, key=lambda x: x[1]))
        self.assertListEqual(list(reversed([(-1, -24), (1, 20), (45, 100), (-24, 356)])),
                             bubblesort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=True, key=lambda x: x[1]))


    def test_heapsort(self):
        self.assertListEqual([-1, 2, 45, 110], heapsort([-1, 2, 45, 110], reverse=False))
        self.assertListEqual(list(reversed([-1, 2, 45, 110])), heapsort([-1, 2, 45, 110], reverse=True))
        self.assertListEqual([], heapsort([]))
        self.assertListEqual(list(range(2, 100)), heapsort(list(range(99, 1, -1))))
        self.assertListEqual([(-24, 356), (-1, -24), (1, 20), (45, 100)],
                             heapsort([(1, 20), (45, 100), (-1, -24), (-24, 356)], key=lambda x: x[0]))
        self.assertListEqual([(-1, -24), (1, 20), (45, 100), (-24, 356)],
                             heapsort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=False, key=lambda x: x[1]))
        self.assertListEqual(list(reversed([(-1, -24), (1, 20), (45, 100), (-24, 356)])),
                             heapsort([(1, 20), (45, 100), (-1, -24), (-24, 356)], reverse=True, key=lambda x: x[1]))
