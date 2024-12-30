from tools.file import read_file_as_chars

from collections import deque


def build_maze(filepath):
    maze = read_file_as_chars(filepath)

    maze_start = None
    maze_end = None
    maze_path = set()

    for r_idx, row in enumerate(maze):
        for c_idx, cell in enumerate(row):
            if cell in "." + "S" + "E":
                cur_loc = (r_idx, c_idx)
                maze_path.add(cur_loc)

                if cell == "S":
                    maze_start = cur_loc
                elif cell == "E":
                    maze_end = cur_loc

    return maze_path, maze_start, maze_end


EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
NORTH = (-1, 0)

# fmt:off
TURN_RIGHT = {
    SOUTH: WEST, 
    WEST: NORTH, 
    NORTH: EAST,
    EAST: SOUTH
    }


# fmt:off
TURN_LEFT = {
    SOUTH: EAST, 
    EAST: NORTH, 
    NORTH: WEST,
    WEST: SOUTH
    }


def bfs_score(path, start, end):
    queue = deque()

    location_scores = {}

    location_scores[start] = (0, 0)  # score, steps
    maze_start = (*start, (0, 1), 0)  # x, y, direction, score
    queue.append(maze_start)

    while queue:
        cur_x, cur_y, cur_dir, cur_score = queue.popleft()

        allowed_directions_and_score = [
            (cur_dir, cur_score + 1),  
            (TURN_LEFT[cur_dir], cur_score + 1001),  
            (TURN_RIGHT[cur_dir], cur_score + 1001), 
        ]

        for new_dir, new_score in allowed_directions_and_score:
            new_x, new_y = cur_x + new_dir[0], cur_y + new_dir[1]
            new_loc = (new_x, new_y)

            if new_loc not in path:
                continue

            _, prev_steps = location_scores.get((cur_x, cur_y), (float('inf'), float('inf')))
            cur_steps = prev_steps + 1

            if new_loc in location_scores:
                old_score, old_steps = location_scores[new_loc]
                if new_score < old_score or (new_score == old_score and cur_steps < old_steps):
                    location_scores[new_loc] = (new_score, cur_steps)
                    queue.append((*new_loc, new_dir, new_score))
            else:
                location_scores[new_loc] = (new_score, cur_steps)
                queue.append((*new_loc, new_dir, new_score))

    return location_scores[end] 

def part1(filepath):
    maze, start, end = build_maze(filepath)

    return bfs_score(maze, start, end)[0]


def recursive_find_paths(
    maze_path,
    current,
    end,
    target_score,
    target_steps,
    current_score,
    current_steps,
    current_dir,
    visited,
    valid_locations,
):
    manhattan_distance = abs(current[0] - end[0]) + abs(current[1] - end[1])

    if current_steps + manhattan_distance > target_steps:
        return

    if current_score > target_score:
        return  

    if current == end:
        if current_score == target_score and current_steps == target_steps:
            valid_locations.update(visited)  
        return

    allowed_directions_and_score = [
        (current_dir, current_score + 1),  
        (TURN_LEFT[current_dir], current_score + 1001),  
        (TURN_RIGHT[current_dir], current_score + 1001),  
    ]

    for new_dir, new_score in allowed_directions_and_score:
        new_x, new_y = current[0] + new_dir[0], current[1] + new_dir[1]
        new_loc = (new_x, new_y)

        if new_loc not in maze_path or new_loc in visited:
            continue

        recursive_find_paths(
            maze_path,
            new_loc,
            end,
            target_score,
            target_steps,
            new_score,
            current_steps + 1,  
            new_dir,
            visited | {new_loc},  
            valid_locations,
        )

def part2(filepath):
    maze_path, start, end = build_maze(filepath)

    target_score, steps  = bfs_score(maze_path, start, end)
    manhattan_distance = abs(start[0]-end[0]) + abs(start[1]-end[1])

    turns = (target_score - steps) // 1000

    print(f"score:{target_score}; man_dist:{manhattan_distance}; steps:{steps}; turns:{turns}")

    valid_locations = set()

    recursive_find_paths(maze_path, current=start, end=end, target_score=target_score, target_steps=steps,  current_score=0, current_steps=0, current_dir=EAST, visited={start}, valid_locations=valid_locations)

    return len(valid_locations)
