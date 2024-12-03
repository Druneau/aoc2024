import day3

INPUT_EXAMPLE = "day3/input_example.txt"
INPUT_EXAMPLE_PART2 = "day3/input_example_part2.txt"
INPUT = "day3/input.txt"


def test_regex_match_mul():
    pattern = f"{day3.PATTERN_MUL}"
    assert day3.get_instructions("mul(1,2)", pattern) == ["mul(1,2)"]
    assert day3.get_instructions("ul(1,2)", pattern) == []
    assert day3.get_instructions("asdfmul(1,2))(@*#)", pattern) == ["mul(1,2)"]
    assert day3.get_instructions("mul(1,2)mul(1,2))(@*#)", pattern) == [
        "mul(1,2)",
        "mul(1,2)",
    ]


def test_execute_instruction():
    assert day3.execute_instruction("mul(1,2)") == 2
    assert day3.execute_instruction("mul(11,8)") == 88


def test_part1():
    assert day3.part1(INPUT_EXAMPLE) == 161
    assert day3.part1(INPUT) == 180233229


def test_get_instructions():
    pattern = f"{day3.PATTERN_MUL}|{day3.PATTERN_DO}|{day3.PATTERN_DONT}"
    assert day3.get_instructions("do()", pattern) == ["do()"]
    assert day3.get_instructions("don't()", pattern) == ["don't()"]
    assert day3.get_instructions("mul(1,2)do()don't()mul(1,2)", pattern) == [
        "mul(1,2)",
        "do()",
        "don't()",
        "mul(1,2)",
    ]


def test_part2():
    assert day3.part2(INPUT_EXAMPLE) == 161
    assert day3.part2(INPUT_EXAMPLE_PART2) == 48
    assert day3.part2(INPUT) == 95411583
