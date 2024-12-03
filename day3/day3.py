import re
import tools.file

PATTERN_MUL = r"mul\(\d+,\d+\)"
PATTERN_DO = r"do\(\)"
PATTERN_DONT = r"don't\(\)"


def get_instructions(line, pattern):
    return re.findall(pattern, line)


def execute_instruction(instruction, do_mul):
    if instruction == "do()":
        do_mul = True
    elif instruction == "don't()":
        do_mul = False
    else:
        if do_mul:
            match = re.search(r"(\d+),(\d+)", instruction)
            num1, num2 = map(int, match.groups())
            return num1 * num2, True

    return 0, do_mul


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

    total_sum = 0
    do_mul = True

    for result, do_mul in (
        execute_instruction(instruction, do_mul) for instruction in instructions
    ):
        total_sum += result

    return total_sum
