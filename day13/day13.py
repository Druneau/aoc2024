from tools.file import read_file_as_strings


def solve_a_b(ax, ay, bx, by, x, y):
    press_count_b = (ax * y - ay * x) / (-ay * bx + ax * by)
    press_count_a = (x - bx * press_count_b) / ax

    return press_count_a, press_count_b


def cost(press_count_a, press_count_b):
    return press_count_a * 3 + press_count_b


def parse_behaviors(filepath):
    behaviors = []
    current_behavior = []
    lines = read_file_as_strings(filepath)
    for line in lines:
        if line.strip() == "":  # Check for empty line
            if current_behavior:  # Add the current group to groups if not empty
                behaviors.append(current_behavior)
                current_behavior = []
        else:
            numbers = [
                int(num)
                for num in line.replace("+", " ")
                .replace("=", " ")
                .replace(",", "")
                .split()
                if num.isdigit()
            ]
            current_behavior.extend(numbers)

    if current_behavior:
        behaviors.append(current_behavior)

    return behaviors


def part1(filepath):
    buttons_behaviors = parse_behaviors(filepath)

    total_cost = 0
    for behavior in buttons_behaviors:
        press_count_a, press_count_b = solve_a_b(*behavior)
        if press_count_a.is_integer() and press_count_b.is_integer():
            total_cost += cost(press_count_a, press_count_b)

    return total_cost
