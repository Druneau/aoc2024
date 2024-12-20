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


def find_cheat_pairs(
    map_of_racetrack, map_size, track_exit_location, max_cheat_distance
):
    r, c = track_exit_location
    cheat_pairs = []

    track_entry_locations = get_locations_within_distance(
        track_exit_location, max_cheat_distance, map_size
    )

    for loc, picoseconds in track_entry_locations:
        r, c = loc
        if map_of_racetrack[r][c] in {".", "S", "E"}:
            cheat_pairs.append(((track_exit_location, loc), picoseconds))

    return cheat_pairs


def get_locations_within_distance(location, distance, map_size):
    row, col = location
    possible_locations = []

    max_row, max_col = map_size
    min_row, min_col = 1, 1

    for dr in range(-distance, distance + 1):
        for dc in range(-distance, distance + 1):
            ortho_distance = abs(dr) + abs(dc)
            if ortho_distance <= distance:
                new_row, new_col = row + dr, col + dc
                if min_row <= new_row < max_row and min_col <= new_col < max_col:
                    possible_locations.append(((new_row, new_col), ortho_distance))

    return possible_locations


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


def count_cheats_above_threshold(filepath, threshold, cheat_picoseconds_limit=2):
    map_of_racetrack = read_file_as_chars(filepath)
    map_rows = len(map_of_racetrack)
    map_cols = len(map_of_racetrack[0])

    racetrack = get_racetrack(map_of_racetrack)

    # find all possible shortcuts with given parameters
    shortcuts = []
    for loc in racetrack:
        shortcuts.extend(
            find_cheat_pairs(
                map_of_racetrack,
                (map_rows, map_cols),
                loc,
                cheat_picoseconds_limit,
            )
        )

    racetrack_location_to_index = {loc: idx for idx, loc in enumerate(racetrack)}

    # calculate how many of the shortcuts give us the same or more savings as threshold
    picoseconds_saved_count = {}
    for shortcut in shortcuts:
        locations, distance = shortcut
        track_exit, track_entry = locations
        index_exit = racetrack_location_to_index[track_exit]
        index_entry = racetrack_location_to_index[track_entry]

        picoseconds_saved = index_entry - index_exit - distance
        if picoseconds_saved > 0:
            picoseconds_saved_count.setdefault(picoseconds_saved, 0)
            picoseconds_saved_count[picoseconds_saved] += 1

    return sum(
        count for saved, count in picoseconds_saved_count.items() if saved >= threshold
    )


def part1(filepath, threshold):
    return count_cheats_above_threshold(filepath, threshold)


def part2(filepath, threshold, cheat_picoseconds_limit):
    return count_cheats_above_threshold(filepath, threshold, cheat_picoseconds_limit)
