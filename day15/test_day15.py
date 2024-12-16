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
    assert day15.shift("[][].") == ".[][]"
    assert day15.shift(".[]") == ".[]"
    assert day15.shift("[][]") == "[][]"
    assert day15.shift("][...") == ".][.."
    assert day15.shift("") == ""


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


def test_widen_warehouse():
    warehouse, _, robot = day15.parse_input("day15/input_simple2.txt")
    widened_warehouse, widened_robot = day15.widen_warehouse(warehouse, robot)

    warehouse_wide, _, robot_wide = day15.parse_input("day15/input_simple2_wide.txt")

    assert widened_warehouse == warehouse_wide
    assert widened_robot == robot_wide


def test_part2():
    assert day15.part2(PATH_EXAMPLE) == 9021
    assert day15.part2(PATH_INPUT) < 1341489
