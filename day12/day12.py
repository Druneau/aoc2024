from tools.file import read_file_as_chars

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

    for row, garden_row in enumerate(garden_map):
        for col, current_plot in enumerate(garden_row):
            valid_touching = get_valid_touching(garden_map, (row, col))

            if current_plot not in plots_by_type:
                plots_by_type[current_plot] = {}

            if (row, col) not in plots_by_type[current_plot]:
                plots_by_type[current_plot][(row, col)] = valid_touching

    return plots_by_type


def get_regions(garden_map) -> dict:
    regions = {}
    plots_by_type = get_plots(garden_map)

    for plot_type, plots in plots_by_type.items():
        split_plots = find_disconnected_regions(plots)
        for region_id, region in enumerate(split_plots):
            regions[f"{plot_type}.{region_id}"] = region

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


def calculate_region_price(region):
    perimeter = sum(4 - len(neighbors) for neighbors in region.values())
    area = len(region)
    return perimeter * area


def calculate_bulk_region_price(region, region_id):
    area = len(region)
    fence_map = get_fence_map(region, region_id[0])
    perimeter = perimeter_scan(fence_map)
    return area * perimeter


def calculate_bulk_price(garden_map):
    regions = get_regions(garden_map)
    return sum(calculate_bulk_region_price(regions[r], r) for r in regions)


def get_fence_map(region, region_id):
    plots = set(region.keys())
    fence_pieces = {
        (row + dr, col + dc)
        for row, col in plots
        for dr, dc in DIRECTIONS
        if (row + dr, col + dc) not in plots
    }

    min_row = min(r for r, _ in fence_pieces)
    max_row = max(r for r, _ in fence_pieces)
    min_col = min(c for _, c in fence_pieces)
    max_col = max(c for _, c in fence_pieces)

    fence_map = [
        [
            "*"
            if (row, col) in fence_pieces
            else region_id
            if (row, col) in plots
            else "."
            for col in range(min_col, max_col + 1)
        ]
        for row in range(min_row, max_row + 1)
    ]

    return fence_map


def nearby_plots(r_id, c_id, fence_map):
    above_match = r_id > 0 and fence_map[r_id - 1][c_id] not in {"*", "."}
    below_match = r_id < len(fence_map) - 1 and fence_map[r_id + 1][c_id] not in {
        "*",
        ".",
    }
    return above_match, below_match


def top_down_fence_count(fence_map):
    perimeter = 0

    for row_idx, row in enumerate(fence_map):
        above, below = False, False

        for col_idx, char in enumerate(row):
            if char == "*":
                cur_above, cur_below = nearby_plots(row_idx, col_idx, fence_map)

                if cur_above and not above:
                    perimeter += 1
                if cur_below and not below:
                    perimeter += 1
                above, below = cur_above, cur_below
            else:
                above, below = False, False
    return perimeter


def perimeter_scan(fence_map):
    row_perimeter = top_down_fence_count(fence_map)
    rotated_fence_map = list(zip(*fence_map))
    col_perimeter = top_down_fence_count(rotated_fence_map)
    return row_perimeter + col_perimeter


def calculate_price(garden_map):
    regions = get_regions(garden_map)
    return sum(calculate_region_price(regions[r]) for r in regions)


def part1(filepath):
    garden_map = read_file_as_chars(filepath)
    return calculate_price(garden_map)


def part2(filepath):
    garden_map = read_file_as_chars(filepath)
    return calculate_bulk_price(garden_map)
