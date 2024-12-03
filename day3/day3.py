import re
import tools.file

PATTERN_MUL = r"mul\(\d+,\d+\)"
PATTERN_DO = r"do\(\)"
PATTERN_DONT = r"don't\(\)"
PATTERN_ALL = f"{PATTERN_MUL}|{PATTERN_DO}|{PATTERN_DONT}"


def get_instructions(line, pattern):
    return re.findall(pattern, line)


def execute_instruction(instruction, do_mul):
    if instruction == "do()":
        return 0, True
    elif instruction == "don't()":
        return 0, False
    elif do_mul:
        match = re.search(r"(\d+),(\d+)", instruction)
        num1, num2 = map(int, match.groups())
        return num1 * num2, True

    return 0, False


def part1(filename):
    lines = tools.file.read_file_as_strings(filename)
    return execute_program(lines, PATTERN_MUL)


def part2(filename):
    lines = tools.file.read_file_as_strings(filename)
    return execute_program(lines, PATTERN_ALL)


def execute_program(lines, pattern):
    instructions = [
        instruction for line in lines for instruction in get_instructions(line, pattern)
    ]

    total_sum = 0
    do_mul = True

    for instruction in instructions:
        result, do_mul = execute_instruction(instruction, do_mul)
        total_sum += result

    return total_sum
