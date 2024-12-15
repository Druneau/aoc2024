import day15

PATH_SIMPLE = "day15/input_simple.txt"
PATH_EXAMPLE = "day15/input_example.txt"
PATH_INPUT = "day15/input.txt"


def test_shift():
    assert day15.shift("O") == "O"
    assert day15.shift(".O") == ".O"
    assert day15.shift("O.") == ".O"
    assert day15.shift("OO") == "OO"
    assert day15.shift("OO.") == ".OO"
    assert day15.shift("OO.....O") == ".OO....O"
    assert day15.shift("OO") == "OO"


def test_parse_input():
    warehouse, moves, robot = day15.parse_input(PATH_SIMPLE)
    assert len(warehouse) == 8
    assert len(moves) == 15
    assert robot == (2, 2)


def test_get_obstacles():
    warehouse, _, robot = day15.parse_input(PATH_SIMPLE)
    assert day15.get_obstacles(warehouse, day15.UP, robot) == "."
    assert day15.get_obstacles(warehouse, day15.RIGHT, robot) == ".O..", "O"
    assert day15.get_obstacles(warehouse, day15.DOWN, robot) == "."
    assert day15.get_obstacles(warehouse, day15.LEFT, robot) == ""


def test_update_boxes():
    warehouse, _, robot = day15.parse_input(PATH_SIMPLE)
    assert day15.update_boxes(warehouse, day15.UP, robot, ["U"]) == [
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", "U", "O", ".", "O", ".", "#"],
        ["#", "#", ".", ".", "O", ".", ".", "#"],
        ["#", ".", ".", ".", "O", ".", ".", "#"],
        ["#", ".", "#", ".", "O", ".", ".", "#"],
        ["#", ".", ".", ".", "O", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    warehouse, _, robot = day15.parse_input(PATH_SIMPLE)
    assert day15.update_boxes(warehouse, day15.RIGHT, robot, [".", ".", "U", "."]) == [
        ["#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", "O", ".", "O", ".", "#"],
        ["#", "#", ".", ".", ".", "U", ".", "#"],
        ["#", ".", ".", ".", "O", ".", ".", "#"],
        ["#", ".", "#", ".", "O", ".", ".", "#"],
        ["#", ".", ".", ".", "O", ".", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#"],
    ]


def test_part1():
    assert day15.part1(PATH_SIMPLE) == 2028
    assert day15.part1(PATH_EXAMPLE) == 10092
    assert day15.part1(PATH_INPUT) == 1318523
