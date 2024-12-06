import os
import curses
import Guard
from tools.file import read_file_as_chars


def generate_map(grid):
    obstructions = []
    position = None
    direction = None

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "#":
                obstructions.append((x, y))
            if position is None:
                if char == "^":
                    direction = (0, -1)
                elif char == ">":
                    direction = (1, 0)
                elif char == "v":
                    direction = (0, 1)
                elif char == "<":
                    direction = (-1, 0)
                if direction:
                    position = (x, y)

    bounds = {"x": len(grid[0]) - 1, "y": len(grid) - 1}

    return position, direction, obstructions, bounds


def part1(filepath, interactive=False):
    grid = read_file_as_chars(filepath)
    position, direction, obstructions, bounds = generate_map(grid)

    guard = Guard.Guard(position, direction, obstructions, bounds)

    if interactive:
        curses.wrapper(guard.run_interactive)
    else:
        while guard.in_sight:
            guard.step_forward()

    return len(guard.visited_positions)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    txt_files = [f for f in os.listdir(script_dir) if f.endswith(".txt")]

    if not txt_files:
        print("No .txt files found.")
        exit(1)

    print("Available files:")
    for i, file in enumerate(txt_files, 1):
        print(f"{i}. {file}")

    try:
        choice = int(input("Enter the number of the file to run: ")) - 1
        if 0 <= choice < len(txt_files):
            selected_file = txt_files[choice]
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        exit(1)

    print(f"You selected: {selected_file}")
    part1(os.path.join(script_dir, selected_file), interactive=True)
