import networkx as nx
from tools.file import read_file_as_chars


def build_paths(filepath):
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

    # build a graph, we can reach if it's in the maze_path
    # and distance is only 1 away in any direction

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    graph = nx.Graph()

    for loc in maze_path:
        r, c = loc
        for dir in directions:
            dr, dc = dir

            neighboor = (r + dr, c + dc)
            if neighboor in maze_path:
                graph.add_edge(loc, neighboor, direction=dir)

    return nx.all_simple_paths(graph, source=maze_start, target=maze_end)


def direction_sensitive_weight(u, v, edge_data, current_direction):
    next_direction = edge_data["direction"]

    if current_direction and current_direction != next_direction:
        return 1001
    return 1


def path_diff(path):
    diff = []
    for a, b in zip(path, path[1:]):
        a_r, a_c = a
        b_r, b_c = b
        diff.append((b_r - a_r, b_c - a_c))
    return diff


def calculate_score(path):
    # a change in direction score +=1000
    # a step in same direction socre +=1

    diff = path_diff(path)

    # START FACING EAST (RIGHT).  POSSIBLY NEED TO TURN ONCE
    if diff[0] != (0, 1):
        diff.insert(0, (0, 1))

    steps = 0
    turns = 0

    for a, b in zip(diff, diff[1:]):
        if a == b:
            steps += 1
        else:
            turns += 1

    # print(f"{steps} steps; {turns} turns")
    return steps + turns * (1000 + 1)


def part1(filepath):
    paths = build_paths(filepath)

    min_score = None

    for path in paths:
        path_score = calculate_score(path)

        if min_score is None:
            min_score = path_score
        else:
            min_score = min(min_score, path_score)

    return min_score
