from tools.file import read_file_as_lists
import numpy as np


def get_trailhead_locations(topo_map):
    return [
        (row_idx, col_idx)
        for row_idx, row in enumerate(topo_map)
        for col_idx, value in enumerate(row)
        if value == 0
    ]


def get_valid_neighbors(array, row, col):
    neighbors = []
    rows, cols = len(array), len(array[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    current_value = array[row][col]
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols:  # Check bounds
            neighbor_value = array[nr][nc]
            if neighbor_value == current_value + 1:  # Condition: value must be +1
                neighbors.append((nr, nc))

    return neighbors


def build_graph(array, start):
    edges = {}
    queue = [start]

    while queue:
        current = queue.pop(0)

        row, col = current
        neighbors = get_valid_neighbors(array, row, col)

        # Always add the current node to the edges
        if current not in edges:
            edges[current] = []

        for neighbor in neighbors:
            queue.append(neighbor)
            edges[current].append(neighbor)  # Add valid neighbors to edges

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


def count_valid_trails(visited_values, topo_map):
    count = 0
    flattened_items = [item for items in visited_values.values() for item in items]
    for row, col in flattened_items:
        if topo_map[row][col] == 9:
            count += 1
    return count


def count_dead_ends_with_value_9(graph, array):
    count = 0
    for node, neighbors in graph.items():
        if not neighbors:
            row, col = node
            if array[row][col] == 9:
                count += 1
    return count


def part1(filepath):
    array = read_file_as_lists(filepath, delimeter=None)
    topo_map = np.array(array)

    trailheads = get_trailhead_locations(topo_map)

    total_score = 0

    for trailhead in trailheads:
        trail_graph = build_graph(topo_map, trailhead)
        score = count_dead_ends_with_value_9(trail_graph, topo_map)
        total_score += score

    return total_score


def part2(filepath):
    array = read_file_as_lists(
        filepath,
        delimeter=None,
        transform=lambda parts: [int(val) if val != "." else -1 for val in parts],
    )
    topo_map = np.array(array)

    sum_ratings = 0

    trailheads = get_trailhead_locations(topo_map)
    for trailhead in trailheads:
        trail_graph = build_graph(topo_map, trailhead)
        ratings = count_valid_trails(trail_graph, topo_map)
        sum_ratings += ratings

    return sum_ratings
