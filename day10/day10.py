from tools.file import read_file_as_lists
import numpy as np


def get_trailhead_locations(topo_map):
    return [
        (row_idx, col_idx)
        for row_idx, row in enumerate(topo_map)
        for col_idx, value in enumerate(row)
        if value == 0
    ]


def get_valid_neighbors(topo_map, row, col):
    rows, cols = len(topo_map), len(topo_map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    current_value = topo_map[row][col]
    return [
        (nr, nc)
        for dr, dc in directions
        if 0 <= (nr := row + dr) < rows
        and 0 <= (nc := col + dc) < cols
        and topo_map[nr][nc] == current_value + 1
    ]


def build_graph(topo_map, start):
    edges = {}
    queue = [start]

    while queue:
        current = queue.pop(0)
        neighbors = get_valid_neighbors(topo_map, *current)

        queue.extend(neighbors)
        edges.setdefault(current, []).extend(neighbors)

    return edges


def pretty_print_graph(graph, array, start, visited=None, prefix="", is_last=True):
    if visited is None:
        visited = set()

    if start in visited:
        return
    visited.add(start)

    row, col = start
    value = array[row][col]
    print(prefix + ("└── " if is_last else "├── ") + f"{value}:({row}, {col})")

    neighbors = graph.get(start, [])
    for i, neighbor in enumerate(neighbors):
        is_last_neighbor = i == len(neighbors) - 1
        pretty_print_graph(
            graph,
            array,
            neighbor,
            visited,
            prefix + ("    " if is_last else "│   "),
            is_last_neighbor,
        )


def count_valid_trails(trail_graph, topo_map):
    count = 0
    flattened_items = [item for items in trail_graph.values() for item in items]
    for row, col in flattened_items:
        if topo_map[row][col] == 9:
            count += 1
    return count


def count_dead_ends_with_value_9(graph, topo_map):
    count = 0
    for node, neighbors in graph.items():
        if not neighbors:
            row, col = node
            if topo_map[row][col] == 9:
                count += 1
    return count


def process_trailheads(filepath, value_count_func=None):
    array = read_file_as_lists(filepath, delimeter=None)
    topo_map = np.array(array)

    total = 0
    trailheads = get_trailhead_locations(topo_map)

    for trailhead in trailheads:
        trail_graph = build_graph(topo_map, trailhead)
        score = value_count_func(trail_graph, topo_map)
        total += score

    return total


def part1(filepath):
    return process_trailheads(
        filepath,
        value_count_func=count_dead_ends_with_value_9,
    )


def part2(filepath):
    return process_trailheads(
        filepath,
        value_count_func=count_valid_trails,
    )
