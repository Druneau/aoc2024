import re
import tools.file

PATTERN_MUL = r"mul\(\d+,\d+\)"


def get_muls(line):
    return re.findall(PATTERN_MUL, line)


def execute_mul(instruction):
    match = re.search(r"(\d+),(\d+)", instruction)
    num1, num2 = map(int, match.groups())
    return num1 * num2


def run_program(filename):
    lines = tools.file.read_file_as_strings(filename)
    instructions = [instruction for line in lines for instruction in get_muls(line)]
    return sum(execute_mul(instruction) for instruction in instructions)
