import os
import time
from multiprocessing import Pool, cpu_count


def parse_map(filepath):
    """
    Parse the input file to extract the initial guard position, direction,
    obstructions, and map bounds.
    """
    with open(filepath) as f:
        grid = [line.strip() for line in f]

    obstructions = set()
    position = None
    direction = None
    directions_map = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "#":
                obstructions.add((x, y))
            elif char in directions_map:
                position = (x, y)
                direction = directions_map[char]

    bounds = {"x": len(grid[0]), "y": len(grid)}
    return position, direction, obstructions, bounds


def simulate_guard(position, direction, obstructions, bounds):
    """
    Simulate the guard's movement until it exits the grid or detects a loop.
    """
    visited = set()
    current_position = position
    current_direction = direction

    while True:
        # Track positions with directions visited
        state = (current_position, current_direction)
        if state in visited:
            return True  # Loop detected
        visited.add(state)

        # Calculate next position
        next_position = (
            current_position[0] + current_direction[0],
            current_position[1] + current_direction[1],
        )

        # Check if out of bounds
        if not (
            0 <= next_position[0] < bounds["x"] and 0 <= next_position[1] < bounds["y"]
        ):
            return False  # Exited the grid

        # Check for obstructions
        if next_position in obstructions:
            # Turn right
            current_direction = (-current_direction[1], current_direction[0])
        else:
            # Move forward
            current_position = next_position


def test_obstruction(test_position, position, direction, obstructions, bounds):
    """
    Test a single obstruction position to determine if it creates a loop.
    """
    return (
        test_position
        if simulate_guard(position, direction, obstructions | {test_position}, bounds)
        else None
    )


def find_valid_obstructions(position, direction, obstructions, bounds):
    """
    Try placing obstructions only on the guard's original path and detect loops using multiprocessing.
    """
    # Precompute the original path
    path = []
    visited = set()
    current_position = position
    current_direction = direction

    while True:
        state = (current_position, current_direction)
        if state in visited:
            break
        visited.add(state)
        path.append(current_position)

        next_position = (
            current_position[0] + current_direction[0],
            current_position[1] + current_direction[1],
        )

        if not (
            0 <= next_position[0] < bounds["x"] and 0 <= next_position[1] < bounds["y"]
        ):
            break

        if next_position in obstructions:
            current_direction = (-current_direction[1], current_direction[0])
        else:
            current_position = next_position

    # Restrict obstruction testing to the path
    path_set = set(path) - {position}
    total_positions = len(path_set)
    start_time = time.time()

    # Use multiprocessing to test obstructions in parallel
    with Pool(processes=cpu_count()) as pool:
        results = pool.starmap(
            test_obstruction,
            [
                (test_position, position, direction, obstructions, bounds)
                for test_position in path_set
            ],
        )

    # Filter out None values from results
    valid_positions = [pos for pos in results if pos]

    elapsed_time = time.time() - start_time
    print(f"\nProcessed {total_positions} positions in {elapsed_time:.2f} seconds.")
    return valid_positions


def part2(filepath):
    # Parse the input map
    position, direction, obstructions, bounds = parse_map(filepath)

    # Find all valid obstruction positions
    valid_positions = find_valid_obstructions(position, direction, obstructions, bounds)

    print(f"Number of valid obstruction positions: {len(valid_positions)}")
    return len(valid_positions)


if __name__ == "__main__":
    # Adjust the file path as needed
    filepath = "day6/input.txt"  # Change to your input file
    if not os.path.exists(filepath):
        print("Input file not found. Please provide the correct path.")
    else:
        part2(filepath)
