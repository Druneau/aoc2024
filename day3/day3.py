import re
import tools.file

PATTERN_MUL = r"mul\(\d+,\d+\)"
PATTERN_INSTRUCTIONS = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"

ENABLED = True


def get_muls(line):
    return re.findall(PATTERN_MUL, line)


def get_instructions(line):
    return re.findall(PATTERN_INSTRUCTIONS, line)


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
    instructions = [instruction for line in lines for instruction in get_muls(line)]
    return sum(execute_instruction(instruction) for instruction in instructions)


def part2(filename):
    lines = tools.file.read_file_as_strings(filename)
    instructions = [
        instruction for line in lines for instruction in get_instructions(line)
    ]
    return sum(execute_instruction(instruction) for instruction in instructions)
