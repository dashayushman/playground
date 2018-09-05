import unittest
import numpy as np

def distance(s1, s2):
    x = len(s1) + 1
    y = len(s2) + 1

    grid = [[-1 for _ in range(x)] for _ in range(y)]

    for i in range(x):
        grid[0][i] = i

    for i in range(y):
        grid[i][0] = i

    for i in range(1, y):
        for j in range(1, x):
            if s1[j - 1] == s2[i - 1]:
                grid[i][j] = grid[i - 1][j - 1]
            else:
                grid[i][j] = min(grid[i - 1][j - 1] + 1,
                                 grid[i][j - 1] + 1,
                                 grid[i - 1][j] + 1)
    print(np.array(grid))
    return grid[x - 1][y - 1]


class Tester(unittest.TestCase):
    def tests(self):
        distance('kitten', 'sitting')
        self.assertEqual(0, distance('bat', 'bat'))
        self.assertEqual(1, distance('bat', 'bam'))
        self.assertEqual(2, distance('bat', 'pot'))
