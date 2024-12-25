import day25


LOCK = """
#####
.####
.####
.####
.#.#.
.#...
.....
"""

KEY = """
.....
#....
#....
#...#
#.#.#
#.###
#####
"""

LOCK_KEY = """
#####
.####
.####
.####
.#.#.
.#...
.....

.....
#....
#....
#...#
#.#.#
#.###
#####
"""


def test_parse_block():
    assert day25.parse_blocks(LOCK) == ([[0, 5, 3, 4, 3]], [])
    assert day25.parse_blocks(KEY) == ([], [[5, 0, 2, 1, 3]])
    assert day25.parse_blocks(LOCK_KEY) == (
        [[0, 5, 3, 4, 3]],
        [[5, 0, 2, 1, 3]],
    )


def test_part1():
    assert day25.part1("day25/input_example.txt") == 3
    assert day25.part1("day25/input.txt") == 3690
