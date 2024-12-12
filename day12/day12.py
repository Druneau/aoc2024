def get_valid_touching(garden_map, plot):
    row, col = plot
    rows, cols = len(garden_map), len(garden_map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    current_plot = garden_map[row][col]
    return [
        (nr, nc)
        for dr, dc in directions
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


def calculate_price(garden_map):
    regions = get_regions(garden_map)

    print()
    return sum(calculate_region_price(regions[r], r) for r in regions)
