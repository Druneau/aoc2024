from tools.file import read_file_as_lists
import numpy as np


def crop_map(array, center, size):
    x_center, y_center = center
    width, height = size

    x_start = max(0, x_center - width // 2)
    x_end = min(len(array), x_center + (width + 1) // 2)
    y_start = max(0, y_center - height // 2)
    y_end = min(len(array[0]), y_center + (height + 1) // 2)

    cropped_map = [row[y_start:y_end] for row in array[x_start:x_end]]
    adjusted_start = (x_center - x_start, y_center - y_start)  # Adjusted start location
    return cropped_map, adjusted_start


def get_trailhead_locations(cropped_map):
    return [
        (row_idx, col_idx)
        for row_idx, row in enumerate(cropped_map)
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
    visited = set()
    visited.add(start)  # Mark the start node as visited immediately

    while queue:
        current = queue.pop(0)
        row, col = current
        neighbors = get_valid_neighbors(array, row, col)
        edges[current] = []

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited when adding to the queue
                queue.append(neighbor)
                edges[current].append(neighbor)  # Add valid neighbor to edges

    return edges


def pretty_print_graph(graph, start, visited=None, prefix="", is_last=True):
    if visited is None:
        visited = set()

    if start in visited:
        return
    visited.add(start)

    print(prefix + ("└── " if is_last else "├── ") + str(start))

    neighbors = graph.get(start, [])
    for i, neighbor in enumerate(neighbors):
        is_last_neighbor = i == len(neighbors) - 1
        pretty_print_graph(
            graph,
            neighbor,
            visited,
            prefix + ("    " if is_last else "│   "),
            is_last_neighbor,
        )


def graph_to_values(graph, array):
    value_graph = {}
    for node, neighbors in graph.items():
        row, col = node
        # Map the node to its value
        value_graph[array[row][col]] = [array[nr][nc] for nr, nc in neighbors]
    return value_graph


def count_valid_trailheads(graph):
    count = 0
    for key, values in graph.items():
        count += values.count(9)  # Count occurrences of 9 in the list of values
    return count


def count_dead_ends_with_value_9(graph, array):
    count = 0
    for node, neighbors in graph.items():
        if not neighbors:  # Check if the node is a dead end
            row, col = node
            if array[row][col] == 9:  # Check if the value at the node is 9
                count += 1
    return count


def part1(filepath, array=None):
    if array is None:
        array = read_file_as_lists(filepath, delimeter=None)
        topo_map = np.array(array)
    else:
        topo_map = array

    trailheads = get_trailhead_locations(topo_map)

    total_score = 0

    for trailhead in trailheads:
        # cropped_map, adjusted_start = crop_map(topo_map, trailhead, (19, 19))
        # trail_graph = build_graph(cropped_map, adjusted_start)
        trail_graph = build_graph(topo_map, trailhead)
        score = count_dead_ends_with_value_9(trail_graph, topo_map)
        total_score += score
        # print(f"h:{trailhead}, score:{score}")
        # pretty_print_graph(trail_graph, trailhead)

    return total_score
