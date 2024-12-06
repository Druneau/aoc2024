import curses


class Guard:
    def __init__(self, position, direction, obstructions, bounds):
        self.position = position
        self.direction = direction
        self.obstructions = set(obstructions)
        self.steps_count = 0
        self.bounds = bounds
        self.in_sight = True
        self.turns_count = 0
        self.visited_positions = []
        self.visited_positions.append(position)
        self.history = []  # Keep a history of moves for reverse stepping

    def is_in_sight(self, location=None):
        if location is None:
            x, y = self.position
        else:
            x, y = location
        x_max, y_max = self.bounds["x"], self.bounds["y"]

        return 0 <= x <= x_max and 0 <= y <= y_max

    def step_forward(self):
        next_position = self.next_position()

        if next_position in self.obstructions:
            self.turn_right()
        else:
            if self.is_in_sight(location=next_position):
                self.history.append((self.position, self.direction))
                self.position = next_position
                self.steps_count += 1
                if self.position not in self.visited_positions:
                    self.visited_positions.append(self.position)
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

    def print_map_old(self, stdscr):

        stdscr.erase()
        max_y, max_x = stdscr.getmaxyx()

        if self.bounds["y"] + 3 >= max_y or self.bounds["x"] + 1 >= max_x:
            stdscr.addstr(0, 0, "Error: Terminal window too small for grid.")
            stdscr.refresh()
            return

        # Draw the grid
        for y in range(-1, self.bounds["y"] + 1):
            for x in range(-1, self.bounds["x"] + 1):
                screen_x, screen_y = x, y + 1
                char = "."
                if (x, y) == self.position:
                    if self.direction == (1, 0):
                        char = ">"
                    elif self.direction == (0, 1):
                        char = "v"
                    elif self.direction == (0, -1):
                        char = "^"
                    elif self.direction == (-1, 0):
                        char = "<"
                elif (x, y) in self.obstructions:
                    char = "#"
                elif (x, y) in self.visited_positions:
                    char = "X"

                if 0 <= screen_y < max_y and 0 <= screen_x < max_x:
                    stdscr.addch(screen_y, screen_x, char)

        info = (
            f"p:{self.position[0]},{self.position[1]}; v:{len(self.visited_positions)}"
        )
        stdscr.addstr(self.bounds["y"] + 2, 0, info[: max_x - 1])
        stdscr.refresh()

    def print_map(self, stdscr):
        """
        Draw the grid on the screen with color:
        - Current guard position in red
        - Obstructions in blue
        """
        curses.start_color()  # Enable color functionality
        curses.init_pair(
            1, curses.COLOR_RED, curses.COLOR_BLACK
        )  # Guard position: Red on black
        curses.init_pair(
            2, curses.COLOR_BLUE, curses.COLOR_BLACK
        )  # Obstructions: Blue on black
        curses.init_pair(
            3, curses.COLOR_WHITE, curses.COLOR_BLACK
        )  # Default: White on black

        stdscr.erase()  # Clear the screen before rendering
        max_y, max_x = stdscr.getmaxyx()  # Get terminal size

        # Check if the grid fits in the terminal
        if self.bounds["y"] + 3 >= max_y or self.bounds["x"] + 1 >= max_x:
            stdscr.addstr(
                0, 0, "Error: Terminal window too small for grid.", curses.color_pair(3)
            )
            stdscr.refresh()
            return

        # Draw the grid
        for y in range(-1, self.bounds["y"] + 1):
            for x in range(-1, self.bounds["x"] + 1):
                screen_x, screen_y = x, y + 1
                char = "."
                color = curses.color_pair(3)  # Default color

                if (x, y) == self.position:
                    if self.direction == (1, 0):
                        char = ">"
                    elif self.direction == (0, 1):
                        char = "v"
                    elif self.direction == (0, -1):
                        char = "^"
                    elif self.direction == (-1, 0):
                        char = "<"
                    color = curses.color_pair(1)  # Red for guard position
                elif (x, y) in self.obstructions:
                    char = "#"
                    color = curses.color_pair(2)  # Blue for obstructions
                elif (x, y) in self.visited_positions:
                    char = "X"

                if 0 <= screen_y < max_y and 0 <= screen_x < max_x:
                    stdscr.addch(screen_y, screen_x, char, color)

        # Add guard information
        info = (
            f"p:{self.position[0]},{self.position[1]}; v:{len(self.visited_positions)}"
        )
        stdscr.addstr(self.bounds["y"] + 2, 0, info[: max_x - 1], curses.color_pair(3))
        stdscr.refresh()

    def update_map(self, stdscr, old_position):
        """
        Update only the necessary parts of the screen when the guard moves.
        - Guard position in red
        - Obstructions in blue
        """
        max_y, max_x = stdscr.getmaxyx()  # Get terminal size

        # Initialize colors (ensure this is called once in your main flow)
        curses.start_color()
        curses.init_pair(
            1, curses.COLOR_RED, curses.COLOR_BLACK
        )  # Red for guard position
        curses.init_pair(
            2, curses.COLOR_BLUE, curses.COLOR_BLACK
        )  # Blue for obstructions
        curses.init_pair(
            3, curses.COLOR_WHITE, curses.COLOR_BLACK
        )  # Default (visited positions)

        # Update the old position
        old_x, old_y = old_position
        if 0 <= old_y + 1 < max_y and 0 <= old_x < max_x:
            stdscr.addch(
                old_y + 1, old_x, "X", curses.color_pair(3)
            )  # Visited position

        # Update the new position
        new_x, new_y = self.position
        if 0 <= new_y + 1 < max_y and 0 <= new_x < max_x:
            char = ">"
            if self.direction == (0, 1):
                char = "v"
            elif self.direction == (0, -1):
                char = "^"
            elif self.direction == (-1, 0):
                char = "<"
            stdscr.addch(
                new_y + 1, new_x, char, curses.color_pair(1)
            )  # Guard position in red

        # Update obstructions (if any are dynamic, otherwise remove this block)
        for obs_x, obs_y in self.obstructions:
            if 0 <= obs_y + 1 < max_y and 0 <= obs_x < max_x:
                stdscr.addch(
                    obs_y + 1, obs_x, "#", curses.color_pair(2)
                )  # Obstructions in blue

        # Update guard information
        info = (
            f"p:{self.position[0]},{self.position[1]}; v:{len(self.visited_positions)}"
        )
        if self.bounds["y"] + 2 < max_y:  # Ensure info fits within the screen
            stdscr.addstr(
                self.bounds["y"] + 2, 0, info[: max_x - 1], curses.color_pair(3)
            )

        stdscr.refresh()

    def update_map_old(self, stdscr, old_position):

        max_y, max_x = stdscr.getmaxyx()

        old_x, old_y = old_position
        if 0 <= old_y + 1 < max_y and 0 <= old_x < max_x:
            stdscr.addch(old_y + 1, old_x, "X")

        new_x, new_y = self.position
        if 0 <= new_y + 1 < max_y and 0 <= new_x < max_x:
            if self.direction == (1, 0):
                stdscr.addch(new_y + 1, new_x, ">")
            elif self.direction == (0, 1):
                stdscr.addch(new_y + 1, new_x, "v")
            elif self.direction == (0, -1):
                stdscr.addch(new_y + 1, new_x, "^")
            elif self.direction == (-1, 0):
                stdscr.addch(new_y + 1, new_x, "<")

        info = (
            f"p:{self.position[0]},{self.position[1]}; v:{len(self.visited_positions)}"
        )
        if self.bounds["y"] + 2 < max_y:  # Ensure info fits within the screen
            stdscr.addstr(self.bounds["y"] + 2, 0, info[: max_x - 1])

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
