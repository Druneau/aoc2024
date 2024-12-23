import networkx as nx
from tools.file import read_file_as_strings


def build_graph(connections):
    lan = nx.Graph()

    for connection in connections:
        computer1, computer2 = connection.split("-")
        lan.add_edge(computer1, computer2)

    return lan


def find_computer_triangles(lan):
    triangles = [
        list(triangle)
        for triangle in nx.enumerate_all_cliques(lan)
        if len(triangle) == 3
    ]

    triangles = [sorted(triangle) for triangle in triangles]

    # we don't care about order
    unique_triangles = sorted(set(tuple(triangle) for triangle in triangles))

    return unique_triangles


def find_employee_lan(lan):
    largest_clique = max(
        (list(clique) for clique in nx.enumerate_all_cliques(lan)), key=len
    )

    return largest_clique


def filter_historian(triangles, char="t"):
    possible_historian_lan = []

    for triangle in triangles:
        if any(computer.startswith(char) for computer in triangle):
            possible_historian_lan.append(triangle)

    return possible_historian_lan


def part1(filepath):
    connections = read_file_as_strings(filepath)

    lan = build_graph(connections)

    sets_of_three = find_computer_triangles(lan)

    historian_lan = filter_historian(sets_of_three)

    return len(historian_lan)


def part2(filepath):
    connections = read_file_as_strings(filepath)

    lan = build_graph(connections)

    employees = find_employee_lan(lan)

    password = ",".join(sorted(employees))

    return password
