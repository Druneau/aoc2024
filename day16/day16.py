from tools.file import read_file_as_chars

from collections import deque


def build_maze(filepath):
    maze = read_file_as_chars(filepath)

    maze_start = None
    maze_end = None
    maze_path = []

    for r_idx, row in enumerate(maze):
        for c_idx, cell in enumerate(row):
            if cell in "." + "S" + "E":
                cur_loc = (r_idx, c_idx)
                maze_path.append(cur_loc)

                if cell == "S":
                    maze_start = cur_loc
                elif cell == "E":
                    maze_end = cur_loc

    return maze_path, maze_start, maze_end


directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def turn_right(cur_dir):
    return directions[
        (directions.index(cur_dir) + 1 + len(directions)) % len(directions)
    ]


def turn_left(cur_dir):
    return directions[
        (directions.index(cur_dir) - 1 + len(directions)) % len(directions)
    ]


def bfs_score(path, start, end):
    queue = deque()

    location_scores = {}

    location_scores[start] = 0

    maze_start = (*start, directions[3], 0)  # x, y, direction, score
    queue.append(maze_start)

    while queue:
        cur_x, cur_y, cur_dir, cur_score = queue.popleft()

        allowed_directions_and_score = [
            (cur_dir, cur_score + 1),
            (turn_left(cur_dir), cur_score + 1001),
            (turn_right(cur_dir), cur_score + 1001),
        ]

        for new_dir, new_score in allowed_directions_and_score:
            new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
            new_loc = (new_x, new_y)

            if new_loc not in path:
                continue

            if new_loc in location_scores:
                if new_score < location_scores[new_loc]:
                    location_scores[new_loc] = new_score
                    queue.append((*new_loc, new_dir, new_score))
            else:
                location_scores[new_loc] = new_score
                queue.append((*new_loc, new_dir, new_score))

    return location_scores[end]


def part1(filepath):
    maze, start, end = build_maze(filepath)

    return bfs_score(maze, start, end)
