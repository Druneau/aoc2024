from tools.file import read_file_as_chars
from tools.print import print_array
from itertools import chain
import time
from collections import deque

BOX = "O"
BOX_LEFT = "["
BOX_RIGHT = "]"
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


def shift_wide(obstacle):
    dot_index = obstacle.find(SPACE)
    if dot_index == -1:
        return obstacle

    return SPACE + obstacle[:dot_index] + obstacle[dot_index + 1 :]


def shift_last(obstacle):
    return obstacle[-1] + obstacle[:-1]


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


def widen_warehouse(warehouse, robot):
    wide_warehouse = []

    for row in warehouse:
        wide_row = []
        for char in row:
            if char == WALL:
                wide_row.extend(["#", "#"])
            if char == BOX:
                wide_row.extend(["[", "]"])
            if char == SPACE:
                wide_row.extend([".", "."])
        wide_warehouse.append(wide_row)

    r, c = robot
    return wide_warehouse, (r, c * 2)


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
    r, c = robot
    dr, dc = get_direction(move)

    obstacles = []

    r += dr
    c += dc

    while warehouse[r][c] != WALL:
        obstacles.append(warehouse[r][c])
        r += dr
        c += dc
    return "".join(obstacles)


def get_wide_obstacles(warehouse, move, robot):
    r, c = robot
    dr, dc = get_direction(move)

    r += dr
    c += dc

    if warehouse[r][c] == SPACE:
        return [(robot, SPACE)]

    # attempt to build a list of locations and things to shift so we can test
    # all of them afterwards and update our warehouse if they can all shift.
    obstacles = []
    pushed_locations = deque([(r, c)])
    visited = set()
    visited.add((c))

    while pushed_locations:
        r, c = pushed_locations.popleft()
        push_start = (r, c)
        obstacle = []
        while warehouse[r][c] not in WALL:
            char = warehouse[r][c]
            obstacle.append(char)
            if char == SPACE:
                break

            if char == BOX_LEFT and move in UP:
                if (c + 1) not in visited:
                    pushed_locations.append((r, c + 1))
                    visited.add((c + 1))
            if char in BOX_RIGHT and move in UP:
                if (c - 1) not in visited:
                    pushed_locations.append((r, c - 1))
                    visited.add((c - 1))
            if char == BOX_LEFT and move in DOWN:
                if (c + 1) not in visited:
                    pushed_locations.append((r, c + 1))
                    visited.add((c + 1))
            if char in BOX_RIGHT and move in DOWN:
                if (c - 1) not in visited:
                    pushed_locations.append((r, c - 1))
                    visited.add((c - 1))

            r += dr
            c += dc

        if obstacle != []:
            obstacles.append([push_start, "".join(obstacle)])

    return obstacles


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


def update_boxes_wide(warehouse, move, robot, shifted_obstacles):
    rows, cols = len(warehouse), len(warehouse[0])
    r, c = robot
    dr, dc = get_direction(move)

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
            if char == BOX or char == "[":
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


def part2(filepath):
    warehouse, moves, robot_loc = parse_input(filepath)

    warehouse, robot_loc = widen_warehouse(warehouse, robot_loc)

    for move in moves:
        if move in RIGHT + LEFT:
            obstacles = [(robot_loc, get_obstacles(warehouse, move, robot_loc))]
        if move in UP + DOWN:
            obstacles = get_wide_obstacles(warehouse, move, robot_loc)

        # can we move?
        can_move = True
        for obstacle in obstacles:
            _, obstacle = obstacle
            shifted = shift_wide(obstacle)
            if not shifted.startswith(SPACE):
                can_move = False
                break

        if obstacles == []:
            can_move = False

        if can_move:
            # yes! now shift everything that needs shifting...
            for obstacle in obstacles:
                start_loc, obstacle = obstacle
                shifted = shift(obstacle)
                print(f"{start_loc}; shifted:{obstacle} --> {shifted}")
                if move in UP + DOWN:
                    warehouse = update_boxes_wide(warehouse, move, start_loc, shifted)
                else:
                    warehouse = update_boxes(warehouse, move, start_loc, shifted)

            warehouse[robot_loc[0]][robot_loc[1]] = SPACE
            dr, dc = get_direction(move)
            r, c = robot_loc
            robot_loc = (r + dr, c + dc)

            warehouse[robot_loc[0]][robot_loc[1]] = ROBOT
            print(f"move:{move}")
            print_array(warehouse)
            input("press key for next...")

    return gps(warehouse)
