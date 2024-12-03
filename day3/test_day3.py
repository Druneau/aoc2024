import day3

INPUT_EXAMPLE = "day3/input_example.txt"
INPUT_EXAMPLE_PART2 = "day3/input_example_part2.txt"
INPUT = "day3/input.txt"


def test_regex_match_mul():
    assert day3.get_muls("mul(1,2)") == ["mul(1,2)"]
    assert day3.get_muls("ul(1,2)") == []
    assert day3.get_muls("asdfmul(1,2))(@*#)") == ["mul(1,2)"]
    assert day3.get_muls("mul(1,2)mul(1,2))(@*#)") == ["mul(1,2)", "mul(1,2)"]


def test_execute_instruction():
    assert day3.execute_instruction("mul(1,2)") == 2
    assert day3.execute_instruction("mul(11,8)") == 88


def test_part1():
    assert day3.part1(INPUT_EXAMPLE) == 161
    assert day3.part1(INPUT) == 180233229


def test_get_instructions():
    assert day3.get_instructions("do()") == ["do()"]
    assert day3.get_instructions("don't()") == ["don't()"]
    assert day3.get_instructions("mul(1,2)do()don't()mul(1,2)") == [
        "mul(1,2)",
        "do()",
        "don't()",
        "mul(1,2)",
    ]


def test_part2():
    assert day3.part2(INPUT_EXAMPLE) == 161
    assert day3.part2(INPUT_EXAMPLE_PART2) == 48
    assert day3.part2(INPUT) == 95411583
