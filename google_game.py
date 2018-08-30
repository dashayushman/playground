import unittest


def get_min_dist(input, current, start, end, mem, dist):
    if current[0] >= len(input) or current[1] >= len(input[0]): return 999999
    elif current[0] < 0 or current[1] < 0: return 999999
    elif input[current[0]][current[1]] == 1: return 999999
    elif current in mem:
        print("blah", current, mem[current], dist)
        return min(mem[current], dist)
    else:
        mem[current] = dist
        mem[(current[0] + 1, current[1])] = get_min_dist(input, (current[0] + 1, current[1]), start, end, mem, dist + 1)
        # up
        mem[(current[0] - 1, current[1])] = get_min_dist(input, (current[0] - 1, current[1]), start, end, mem, dist + 1)
        # right
        mem[(current[0], current[1] + 1)] = get_min_dist(input, (current[0], current[1] + 1), start, end, mem, dist + 1)
        # left
        mem[(current[0], current[1] - 1)] = get_min_dist(input, (current[0], current[1] - 1), start, end, mem, dist + 1)

    return mem[(current[0], current[1] - 1)]


def get_sol(input, start, end, mem):
    get_min_dist(input, start, start, end, mem, 0)
    print(mem)
    if end not in mem:
        return None
    else:
        return mem[end]


class Tester(unittest.TestCase):
    def tests(self):
        input = [[0, 0, 0, 0],
                 [1, 1, 0, 1],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        target = 7
        start = (3, 0)
        end = (0, 0)
        self.assertEquals(target, get_sol(input, start, end, {}))