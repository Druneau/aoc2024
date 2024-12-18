import day18


def test_part1():
    assert day18.part1("day18/input_example.txt", bytes_fallen=12, memory_size=6) == 22
    assert day18.part1("day18/input.txt", bytes_fallen=1024, memory_size=70) == 436


def test_part2():
    assert day18.part2("day18/input_example.txt", bytes_fallen=0, memory_size=6) == (
        6,
        1,
    )

    assert day18.part2("day18/input.txt", bytes_fallen=0, memory_size=70) == (
        6,
        1,
    )
