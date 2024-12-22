import day22


def test_mix():
    assert day22.mix(secret=42, number=15) == 37


def test_prune():
    assert day22.prune(secret=100000000) == 16113920


def test_evolve_secret():
    assert day22.evolve_secret(secret=123) == 15887950
    assert day22.evolve_secret(secret=15887950) == 16495136
    assert day22.evolve_secret(secret=16495136) == 527345
    assert day22.evolve_secret(secret=527345) == 704524
    assert day22.evolve_secret(secret=704524) == 1553684
    assert day22.evolve_secret(secret=1553684) == 12683156
    assert day22.evolve_secret(secret=12683156) == 11100544
    assert day22.evolve_secret(secret=11100544) == 12249484
    assert day22.evolve_secret(secret=12249484) == 7753432
    assert day22.evolve_secret(secret=7753432) == 5908254


def test_part1():
    assert day22.part1("day22/input_example.txt", 2000) == 37327623
    assert day22.part1("day22/input.txt", 2000) == 14691757043


def test_part2():
    assert day22.part2("day22/input_example_part2.txt", 2000) == 23
    assert day22.part2("day22/input.txt", 2000) == 1831
