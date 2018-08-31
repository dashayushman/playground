import unittest


def is_valid_move(row, col, board):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    return not board[row][col]

def get_next_elements(c, game):
    return [e for e in [(c[0] + 1, c[1]), (c[0] - 1, c[1]),
                        (c[0], c[1] + 1), (c[0], c[1] - 1)]
            if is_valid_move(e[0], e[1], game)]


def get_walkable_neighbours(board, row, col):
    return [(r, c) for r, c in [
        (row, col - 1),
        (row - 1, col),
        (row + 1, col),
        (row, col + 1)]
        if is_valid_move(r, c, board)
    ]

def shortest_path(board, start, end):
    seen = set()
    queue = [(start, 0)]
    while queue:
        coords, count = queue.pop(0)
        if coords == end:
            return count
        seen.add(coords)
        neighbours = get_walkable_neighbours(board, coords[0], coords[1])
        queue.extend((neighbour, count + 1) for neighbour in neighbours
                if neighbour not in seen)


def solve(input, start, end):
    if start == end:
        return 0
    seen = set()
    q = [(start, 0)]
    while q:
        element, count = q.pop(0)
        if element == end:
            return count
        seen.add(element)
        neighbours = get_next_elements(element, input)
        q.extend((n, count + 1) for n in neighbours if n not in seen)



class Tester(unittest.TestCase):
    def tests(self):
        input = [[0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
        target = None
        start = (3, 0)
        end = (0, 0)
        self.assertEqual(target, shortest_path(input, start, end))
