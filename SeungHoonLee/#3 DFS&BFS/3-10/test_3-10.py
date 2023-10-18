from unittest import TestCase
from sol import generate_next_pos


class Test(TestCase):
    def test_generate_next_pos(self):
        board: list[list[int]] = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        next_post: list[set[tuple]] = generate_next_pos({(1, 1), (1, 2)}, board)
        self.assertEqual(4, len(next_post))

        next_post: list[set[tuple]] = generate_next_pos({(1, 3), (2, 3)}, board)
        self.assertEqual(4, len(next_post))

        next_post: list[set[tuple]] = generate_next_pos({(2, 3), (3, 3)}, board)
        self.assertEqual(2, len(next_post))

        next_post: list[set[tuple]] = generate_next_pos({(3, 3), (4, 3)}, board)
        self.assertEqual(2, len(next_post))

        next_post: list[set[tuple]] = generate_next_pos({(4, 3), (5, 3)}, board)
        self.assertEqual(4, len(next_post))

        next_post: list[set[tuple]] = generate_next_pos({(5, 3), (5, 4)}, board)
        self.assertEqual(5, len(next_post))
