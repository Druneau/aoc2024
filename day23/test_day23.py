import day23


def test_part1():
    assert day23.part1("day23/input_example.txt") == 7
    assert day23.part1("day23/input.txt") == 1378


def test_part2():
    assert day23.part2("day23/input_example.txt") == "co,de,ka,ta"
    assert day23.part2("day23/input.txt") == "bs,ey,fq,fy,he,ii,lh,ol,tc,uu,wl,xq,xv"
