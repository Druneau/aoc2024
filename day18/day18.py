from tools.file import read_file_as_tuples
import networkx as nx


def calculate_shortest_path(corrupted_positions, memory_size):
    safe_memory = set(
        (r, c)
        for r in range(memory_size + 1)
        for c in range(memory_size + 1)
        if (r, c) not in corrupted_positions
    )

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start = (0, 0)
    exit = (memory_size, memory_size)

    graph = nx.Graph()

    for loc in safe_memory:
        r, c = loc
        for dr, dc in directions:
            neighboor = (r + dr, c + dc)
            if neighboor in safe_memory:
                graph.add_edge(loc, neighboor)
    try:
        return nx.shortest_path_length(graph, source=start, target=exit)
    except nx.NetworkXNoPath:
        return -1


def compute_steps(bytes_fall_order, count, memory_size):
    steps_to_exit = calculate_shortest_path(bytes_fall_order[:count], memory_size)
    print(f"{steps_to_exit} steps to exit when {count} bytes have fallen")
    return steps_to_exit


def part1(filepath, bytes_fallen, memory_size):
    bytes_fall_order = read_file_as_tuples(filepath)
    return compute_steps(bytes_fall_order, bytes_fallen, memory_size)


def part2(filepath, memory_size):
    bytes_fall_order = read_file_as_tuples(filepath)
    path, no_path = 0, len(bytes_fall_order) - 1
    result = None

    while path <= no_path:
        try_path = (path + no_path) // 2
        steps_to_exit = compute_steps(bytes_fall_order, try_path + 1, memory_size)

        if steps_to_exit == -1:
            result = bytes_fall_order[try_path]
            no_path = try_path - 1
        else:
            path = try_path + 1

    return result
