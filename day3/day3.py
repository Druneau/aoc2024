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
    instructions = [
        instruction
        for line in lines
        for instruction in get_instructions(line, PATTERN_MUL)
    ]
    return sum(execute_instruction(instruction) for instruction in instructions)


def part2(filename):
    lines = tools.file.read_file_as_strings(filename)
    pattern_instructions = f"{PATTERN_MUL}|{PATTERN_DO}|{PATTERN_DONT}"
    instructions = [
        instruction
        for line in lines
        for instruction in get_instructions(line, pattern_instructions)
    ]
    return sum(execute_instruction(instruction) for instruction in instructions)
