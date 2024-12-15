from tools.file import read_file_as_chars
from tools.print import print_array
from itertools import chain
import time

BOX = "O"
WALL = "#"
SPACE = "."
ROBOT = "@"
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


def shift(obstacles):
    dot_index = obstacles.find(SPACE)
    if dot_index == -1:
        return obstacles

    return SPACE + obstacles[:dot_index] + obstacles[dot_index + 1 :]


def parse_input(filepath):
    lines = read_file_as_chars(filepath)

    warehouse = [line for line in lines if line and line[0] == WALL]
    moves = [line for line in lines if line and not line[0] == WALL]
    moves = list(chain.from_iterable(moves))

    robot_row = 0
    robot_col = 0

    # find robot in warehouse
    for row_idx, row in enumerate(warehouse):
        for col_idx, char in enumerate(row):
            if char == ROBOT:
                robot_row = row_idx
                robot_col = col_idx
                # we have robot, don't need it anymore
                warehouse[row_idx][col_idx] = SPACE

    return warehouse, moves, (robot_row, robot_col)


def get_direction(move):
    if move == UP:
        return (-1, 0)
    if move == RIGHT:
        return (0, 1)
    if move == DOWN:
        return (1, 0)
    if move == LEFT:
        return (0, -1)


def get_obstacles(warehouse, move, robot):
    rows, cols = len(warehouse), len(warehouse[0])
    r, c = robot
    dr, dc = get_direction(move)

    obstacles = []

    r += dr
    c += dc

    while 0 <= r < rows and 0 <= c < cols:
        if warehouse[r][c] == WALL:
            break
        obstacles.append(warehouse[r][c])
        r += dr
        c += dc
    return "".join(obstacles)


def update_boxes(warehouse, move, robot, shifted_obstacles):
    rows, cols = len(warehouse), len(warehouse[0])
    r, c = robot
    dr, dc = get_direction(move)

    r += dr
    c += dc

    # move robot
    robot = (r, c)

    for char in shifted_obstacles:
        if 0 <= r < rows and 0 <= c < cols:
            warehouse[r][c] = char
        else:
            break
        r += dr
        c += dc

    return warehouse


def gps(warehouse):
    sum_gps = 0
    for r_idx, row in enumerate(warehouse):
        for c_idx, char in enumerate(row):
            if char == BOX:
                sum_gps += c_idx + r_idx * 100
    return sum_gps


def part1(filepath):
    warehouse, moves, robot = parse_input(filepath)
    # need to go through all the moves
    for move in moves:
        obstacles = get_obstacles(warehouse, move, robot)

        shifted_obstacles = shift(obstacles)
        if shifted_obstacles.startswith(SPACE):
            # we can move!
            warehouse = update_boxes(warehouse, move, robot, shifted_obstacles)
            dr, dc = get_direction(move)
            r, c = robot
            robot = (r + dr, c + dc)

    return gps(warehouse)
