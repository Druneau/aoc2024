import re
import tools.file

PATTERN_MUL = r"mul\(\d+,\d+\)"
PATTERN_DO = r"do\(\)"
PATTERN_DONT = r"don't\(\)"

ENABLED = True


def get_instructions(line, pattern):
    return re.findall(pattern, line)


def execute_instruction(instruction):
    global ENABLED
    if instruction == "do()":
        ENABLED = True
    elif instruction == "don't()":
        ENABLED = False
    else:
        if ENABLED:
            match = re.search(r"(\d+),(\d+)", instruction)
            num1, num2 = map(int, match.groups())
            return num1 * num2

    return 0


def part1(filename):
    lines = tools.file.read_file_as_strings(filename)
    return execute_program(lines, PATTERN_MUL)


def part2(filename):
    lines = tools.file.read_file_as_strings(filename)
    return execute_program(lines, f"{PATTERN_MUL}|{PATTERN_DO}|{PATTERN_DONT}")


def execute_program(lines, pattern):
    instructions = [
        instruction for line in lines for instruction in get_instructions(line, pattern)
    ]
    return sum(execute_instruction(instruction) for instruction in instructions)
