import curses
import time


class Guard:
    def __init__(self, position, direction, obstructions, bounds):
        self.position = position
        self.direction = direction
        self.obstructions = set(obstructions)
        self.steps_count = 0
        self.bounds = bounds
        self.in_sight = True
        self.turns_count = 0
        self.visited_positions = set()
        self.visited_positions.add(position)
        self.history = []  # Keep a history of moves for reverse stepping
        self.loop_opportunity = set()
        self.hit_obstructions = {}

    def is_in_sight(self, location=None):
        if location is None:
            x, y = self.position
        else:
            x, y = location
        x_max, y_max = self.bounds["x"], self.bounds["y"]

        return 0 <= x <= x_max and 0 <= y <= y_max

    def record_hit_obstruction(self, obstruction_position):
        """
        Record an obstruction hit with the direction it was hit from.
        """
        if obstruction_position not in self.hit_obstructions:
            self.hit_obstructions[obstruction_position] = set()
        self.hit_obstructions[obstruction_position].add(self.direction)

    def has_hit_obstruction(self, obstruction_position, direction):
        """
        Check if the obstruction at the given position was already hit from the specified direction.
        """
        return direction in self.hit_obstructions.get(obstruction_position, set())

    def step_forward(self):
        next_position = self.next_position()

        if next_position in self.obstructions:
            self.record_hit_obstruction(next_position)
            self.turn_right()
        else:
            if self.is_in_sight(location=next_position):
                if self.obstruction_right():
                    if next_position not in self.obstructions:
                        if next_position not in self.loop_opportunity:
                            self.loop_opportunity.add(next_position)

                self.history.append((self.position, self.direction))
                self.position = next_position
                self.steps_count += 1
                self.visited_positions.add(self.position)
                self.in_sight = True

            else:
                self.in_sight = False

    def step_backward(self):
        if self.history:
            self.position, self.direction = self.history.pop()
            self.steps_count -= 1
        else:
            pass

    def turn_right(self):
        x, y = self.direction
        self.direction = (-y, x)
        self.turns_count += 1

    def next_position(self):
        return (
            self.position[0] + self.direction[0],
            self.position[1] + self.direction[1],
        )

    def obstruction_right(self):
        x, y = self.direction
        right_direction = (-y, x)

        current_position = self.position

        while self.is_in_sight(current_position):
            current_position = (
                current_position[0] + right_direction[0],
                current_position[1] + right_direction[1],
            )

            if self.has_hit_obstruction(current_position, right_direction):
                return True

        return False

    def print_map(self, stdscr):

        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        stdscr.erase()
        max_y, max_x = stdscr.getmaxyx()

        if self.bounds["y"] + 3 >= max_y or self.bounds["x"] + 1 >= max_x:
            stdscr.addstr(
                0, 0, "Error: Terminal window too small for grid.", curses.color_pair(3)
            )
            stdscr.refresh()
            return

        for y in range(-1, self.bounds["y"] + 1):
            for x in range(-1, self.bounds["x"] + 1):
                screen_x, screen_y = x, y + 1
                char = "."
                color = curses.color_pair(3)

                if (x, y) == self.position:
                    if self.direction == (1, 0):
                        char = ">"
                    elif self.direction == (0, 1):
                        char = "v"
                    elif self.direction == (0, -1):
                        char = "^"
                    elif self.direction == (-1, 0):
                        char = "<"
                    color = curses.color_pair(1)
                elif (x, y) in self.obstructions:
                    char = "#"
                    color = curses.color_pair(2)
                elif (x, y) in self.visited_positions:
                    char = "X"

                if 0 <= screen_y < max_y and 0 <= screen_x < max_x:
                    stdscr.addch(screen_y, screen_x, char, color)

        info = f"p:{self.position[0]},{self.position[1]}; v:{len(self.visited_positions)}; l:{len(self.loop_opportunity)}"
        stdscr.addstr(self.bounds["y"] + 2, 0, info[: max_x - 1], curses.color_pair(3))
        stdscr.refresh()

    def update_map(self, stdscr, old_position):
        max_y, max_x = stdscr.getmaxyx()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        old_x, old_y = old_position
        if 0 <= old_y + 1 < max_y and 0 <= old_x < max_x:
            if (old_x, old_y) in self.loop_opportunity:
                stdscr.addch(old_y + 1, old_x, "O", curses.color_pair(4))
            else:
                stdscr.addch(old_y + 1, old_x, "X", curses.color_pair(3))

        new_x, new_y = self.position
        if 0 <= new_y + 1 < max_y and 0 <= new_x < max_x:
            char = ">"
            if self.direction == (0, 1):
                char = "v"
            elif self.direction == (0, -1):
                char = "^"
            elif self.direction == (-1, 0):
                char = "<"
            stdscr.addch(new_y + 1, new_x, char, curses.color_pair(1))  # Guard in red

        for obs_x, obs_y in self.obstructions:
            if 0 <= obs_y + 1 < max_y and 0 <= obs_x < max_x:
                if (obs_x, obs_y) in self.hit_obstructions:
                    stdscr.addch(obs_y + 1, obs_x, "#", curses.color_pair(1))
                else:
                    stdscr.addch(obs_y + 1, obs_x, "#", curses.color_pair(2))

        info = f"p:{self.position[0]},{self.position[1]}; v:{len(self.visited_positions)}; l:{len(self.loop_opportunity)}"
        if self.bounds["y"] + 2 < max_y:
            stdscr.addstr(
                self.bounds["y"] + 2, 0, info[: max_x - 1], curses.color_pair(3)
            )

        status_y = self.bounds["y"] + 2
        if status_y < max_y:
            stdscr.move(status_y, 0)  # Move to the start of the status line
            stdscr.clrtoeol()  # Clear from the cursor to the end of the line

        if status_y < max_y:
            stdscr.addstr(status_y, 0, info[: max_x - 1], curses.color_pair(3))

        stdscr.refresh()

    def run_interactive(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(True)

        self.print_map(stdscr)

        while True:
            old_position = self.position
            key = stdscr.getch()

            if key == curses.KEY_RIGHT:
                self.step_forward()
            elif key == curses.KEY_LEFT:
                self.step_backward()
            elif key == ord("q"):
                break  # Exit on 'q' key
            else:
                continue

            self.update_map(stdscr, old_position)
            time.sleep(0.1)
