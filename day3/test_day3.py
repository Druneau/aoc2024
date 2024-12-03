import day3

INPUT_EXAMPLE = "day3/input_example.txt"
INPUT = "day3/input.txt"


def test_regex_match_mul():
    assert day3.get_muls("mul(1,2)") == ["mul(1,2)"]
    assert day3.get_muls("ul(1,2)") == []
    assert day3.get_muls("asdfmul(1,2))(@*#)") == ["mul(1,2)"]
    assert day3.get_muls("mul(1,2)mul(1,2))(@*#)") == ["mul(1,2)", "mul(1,2)"]


def test_execute_mul():
    assert day3.execute_mul("mul(1,2)") == 2
    assert day3.execute_mul("mul(11,8)") == 88


def test_run_program():
    assert day3.run_program(INPUT_EXAMPLE) == 161
    assert day3.run_program(INPUT) == 180233229
