from tools.file import read_file_as_chars


def get_racetrack(map_of_racetrack):
    start = None
    for r_idx, row in enumerate(map_of_racetrack):
        for c_idx, cell in enumerate(row):
            if cell == "S":
                start = (r_idx, c_idx)
                break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    racetrack = []
    current = start

    while True:
        racetrack.append(current)  # Add the current position to the path

        if map_of_racetrack[current[0]][current[1]] == "E":
            break  # Stop when we reach "E"

        for dr, dc in directions:
            # Check the neighboring cell
            nr, nc = current[0] + dr, current[1] + dc
            if (
                0 <= nr < len(map_of_racetrack)
                and 0 <= nc < len(map_of_racetrack[0])
                and (nr, nc) not in racetrack  # Ensure we don't revisit
                and map_of_racetrack[nr][nc] in {".", "E"}  # Valid next step
            ):
                current = (nr, nc)
                break

    return racetrack


def find_cheat_pairs(map_of_racetrack, location):
    r, c = location
    cheat_pairs = []

    # Check left-right pair
    if map_of_racetrack[r][c - 1] in {".", "S", "E"} and map_of_racetrack[r][c + 1] in {
        ".",
        "S",
        "E",
    }:
        cheat_pairs.append(((r, c - 1), (r, c + 1)))

    # Check above-below pair
    if map_of_racetrack[r - 1][c] in {".", "S", "E"} and map_of_racetrack[r + 1][c] in {
        ".",
        "S",
        "E",
    }:
        cheat_pairs.append(((r - 1, c), (r + 1, c)))

    return cheat_pairs


def print_racetrack(racetrack_locations, shortcut_location):
    # Determine the bounds of the racetrack
    max_row = max(loc[0] for loc in racetrack_locations)
    max_col = max(loc[1] for loc in racetrack_locations)

    # Create a set for fast lookup of shortcut locations
    shortcut_set = set(shortcut_location)
    start = racetrack_locations[0]
    end = racetrack_locations[-1]

    for r in range(max_row + 1):
        line = []
        for c in range(max_col + 1):
            loc = (r, c)
            if loc == start:
                line.append("S")
            elif loc == end:
                line.append("E")
            elif loc in shortcut_set:
                line.append("X")
            elif loc in racetrack_locations:
                line.append(".")
            else:
                line.append("#")
        print("".join(line))


def part1(filepath, threshold):
    map_of_racetrack = read_file_as_chars(filepath)

    shortcuts = []

    for row_index in range(1, len(map_of_racetrack) - 1):
        for col_index in range(1, len(map_of_racetrack) - 1):
            if map_of_racetrack[row_index][col_index] == "#":
                shortcuts.extend(
                    find_cheat_pairs(map_of_racetrack, (row_index, col_index))
                )

    racetrack = get_racetrack(map_of_racetrack)
    racetrack_location_to_index = {loc: idx for idx, loc in enumerate(racetrack)}
    picoseconds_saved_count = {}

    for shortcut in shortcuts:
        track_exit, track_entry = shortcut
        index_exit = racetrack_location_to_index[track_exit]
        index_entry = racetrack_location_to_index[track_entry]

        index_exit_track = min(index_exit, index_entry)
        index_entry_track = max(index_exit, index_entry)

        picoseconds_saved = index_entry_track - index_exit_track - 2
        picoseconds_saved_count.setdefault(picoseconds_saved, 0)
        picoseconds_saved_count[picoseconds_saved] += 1

    return sum(
        count for saved, count in picoseconds_saved_count.items() if saved >= threshold
    )
