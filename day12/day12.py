from tools.file import read_file_as_chars
from tools.print import print_array
from collections import Counter

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_valid_touching(garden_map, plot):
    row, col = plot
    rows, cols = len(garden_map), len(garden_map[0])

    current_plot = garden_map[row][col]
    return [
        (nr, nc)
        for dr, dc in DIRECTIONS
        if 0 <= (nr := row + dr) < rows
        and 0 <= (nc := col + dc) < cols
        and garden_map[nr][nc] == current_plot
    ]


def get_plots(garden_map) -> dict:
    plots_by_type = {}

    height = len(garden_map)
    width = len(garden_map[0])
    for row in range(height):
        for col in range(width):
            current_plot = garden_map[row][col]
            valid_touching = get_valid_touching(garden_map, (row, col))
            dict_current_plot = plots_by_type.setdefault(current_plot, {})
            dict_current_plot.setdefault((row, col), valid_touching)

    return plots_by_type


def get_regions(garden_map) -> dict:
    regions = {}
    plots_by_type = get_plots(garden_map)

    for type, plots in plots_by_type.items():
        split_plots = find_disconnected_regions(plots)
        for id, r in enumerate(split_plots):
            regions.setdefault(type + "." + str(id), r)

    return regions


def find_disconnected_regions(plot_type):
    def dfs(node, visited, component):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                component[current] = plot_type[current]
                for neighbor in plot_type[current]:
                    if neighbor in plot_type and neighbor not in visited:
                        stack.append(neighbor)

    visited = set()
    components = []

    for node in plot_type:
        if node not in visited:
            component = {}
            dfs(node, visited, component)
            components.append(component)

    return components


def calculate_region_price(region, id):
    perimeter = sum(4 - len(values) for values in region.values())
    area = len(region)

    # print(f"{id}, {area} * {perimeter} = {perimeter * area}")

    return perimeter * area


def calculate_bulk_region_price(region, id):
    area = len(region)
    fence_map, overlaps = get_fence_map(region, id[0])

    # need to count how many regions of type "F" FOR FENCE!
    fence_regions = get_regions(fence_map)

    perimeter = sum(1 for f in fence_regions.keys() if f.startswith("*"))

    print(f"a:{area} * p:{perimeter+overlaps} = {area *(perimeter+overlaps)}")

    return area * (perimeter + overlaps)


def calculate_bulk_price(garden_map):
    regions = get_regions(garden_map)

    return sum(calculate_bulk_region_price(regions[r], r) for r in regions)


def get_fence_map(region, id):
    plots = set(region.keys())
    fence_pieces = []

    for row, col in plots:
        for dr, dc in DIRECTIONS:
            neighbor = (row + dr, col + dc)
            if neighbor not in plots:
                fence_pieces.append(neighbor)

    # build a fence map!
    max_col = max(piece[1] for piece in fence_pieces)
    max_row = max(piece[0] for piece in fence_pieces)
    min_col = min(piece[1] for piece in fence_pieces)
    min_row = min(piece[0] for piece in fence_pieces)
    fence_map = []

    for row in range(min_row, max_row + 1):
        map_row = []
        for col in range(min_col, max_col + 1):
            current_plot = (row, col)
            if current_plot in fence_pieces:
                map_row.append("*")
            elif current_plot in plots:
                map_row.append(id)
            else:
                map_row.append(".")
        fence_map.append(map_row)
    print_array(fence_map)
    return (fence_map, count_duplicates(fence_pieces))


def count_duplicates(values):
    counts = Counter(values)
    doubles = sum(1 for count in counts.values() if count == 2)
    triples = sum(1 for count in counts.values() if count == 3)
    return [doubles, triples]


def calculate_price(garden_map):
    regions = get_regions(garden_map)

    return sum(calculate_region_price(regions[r], r) for r in regions)


def part1(filepath):
    garden_map = read_file_as_chars(filepath)
    return calculate_price(garden_map)


def part2(filepath):
    print("asdf")
    garden_map = read_file_as_chars(filepath)
    return calculate_bulk_price(garden_map)
