import day14

PATH_SINGLE = "day14/input_single.txt"
PATH_EXAMPLE = "day14/input_example.txt"
PATH_INPUT = "day14/input.txt"


def test_parse_input():
    assert day14.parse_input(PATH_SINGLE) == [[(0, 4), (3, -3)]]


def test_step():
    map_size = (11, 7)
    # teleport across all 4 corners
    assert day14.step((0, 0), (-1, -1), map_size) == (10, 6)
    assert day14.step((10, 0), (1, -1), map_size) == (0, 6)
    assert day14.step((0, 6), (-1, 1), map_size) == (10, 0)
    assert day14.step((10, 6), (1, 1), map_size) == (0, 0)

    assert day14.step((2, 4), (2, -3), map_size) == (4, 1)


def test_calculate_positions():
    # robot across same diagonal
    robot = [(0, 0), (1, 1)]
    map_size = [10, 10]
    assert len(day14.calculate_positions(robot, map_size)) == 10


def test_pos_after_seconds():
    robot = [(2, 4), (2, -3)]
    map_size = (11, 7)
    positions = day14.calculate_positions(robot, map_size)
    assert day14.pos_after_seconds(positions, seconds=0) == (2, 4)
    assert day14.pos_after_seconds(positions, seconds=5) == (1, 3)
    # full circle
    assert day14.pos_after_seconds(positions, seconds=77) == (
        2,
        4,
    )


def test_part1():
    assert day14.part1(PATH_EXAMPLE, (11, 7)) == 12
    assert day14.part1(PATH_INPUT, (101, 103)) == 216027840


def test_part2():
    assert day14.part2(PATH_INPUT, (101, 103)) == 6876
