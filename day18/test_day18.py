import day18


def test_part1():
    assert day18.part1("day18/input_example.txt", bytes_fallen=12, memory_size=6) == 22
    assert day18.part1("day18/input.txt", bytes_fallen=1024, memory_size=70) == 22
