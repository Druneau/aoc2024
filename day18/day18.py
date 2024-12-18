from tools.file import read_file_as_tuples
import networkx as nx


def shortest_steps(fallen_bytes, memory_size):
    non_corrupted_memory = set()
    for r in range(memory_size + 1):
        for c in range(memory_size + 1):
            if (c, r) not in fallen_bytes:
                non_corrupted_memory.add((c, r))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    memory_entry = (0, 0)
    memory_exit = (memory_size, memory_size)
    graph = nx.Graph()

    for loc in non_corrupted_memory:
        r, c = loc
        for dir in directions:
            dr, dc = dir

            neighboor = (r + dr, c + dc)
            if neighboor in non_corrupted_memory:
                graph.add_edge(loc, neighboor, direction=dir)

    return nx.shortest_path_length(graph, source=memory_entry, target=memory_exit)


def part1(filepath, bytes_fallen, memory_size):
    bytes_fall_order = read_file_as_tuples(filepath)

    steps_to_exit = shortest_steps(bytes_fall_order[:bytes_fallen], memory_size)
    print(f"{steps_to_exit} steps to exit when {bytes_fallen} have fallen")

    return steps_to_exit