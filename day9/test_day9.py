import day9


def test_part1():
    assert day9.part1("day9/input_example.txt") == 1928
    assert day9.part1("day9/input.txt") == 6288599492129


def test_to_blocks():
    # fmt: off
    assert day9.to_blocks("2333133121414131402") == [
        0, 0, ".", ".", ".", 1, 1, 1, ".", ".", ".", 2, ".", ".",
        ".", 3, 3, 3, ".", 4, 4, ".", 5, 5, 5, 5, ".", 6, 6, 6, 6,
        ".", 7, 7, 7, ".", 8, 8, 8, 8, 9, 9, 
    ]


def test_per_block_compact():
    # fmt:off
    assert day9.per_block_compact([0,0,".",".",".",1,1,1,".",".",".",2,".",
                         ".",".",3,3,3,".",4,4,".",5,5,5,5,".",6,
                         6,6,6,".",7,7,7,".",8,8,8,8,9,9,]
                         
                        ) == [

                         0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,
                         4,6,5,5,5,5,6,6,
    ]


def test_checksum():
    # fmt: off
    assert (
        day9.checksum(
            [0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6,]
        ) == 1928
    )


def test_blocks_to_files():
    assert day9.blocks_to_files([1, 2, 3]) == ([(0, 1, 1), (1, 1, 2), (2, 1, 3)])
    assert day9.blocks_to_files([1, 2, 3, 3]) == ([(0, 1, 1), (1, 1, 2), (2, 2, 3)])
    assert day9.blocks_to_files([1, ".", 3, 3]) == ([(0, 1, 1), (1, 1, "."), (2, 2, 3)])
    assert day9.blocks_to_files([".", ".", ".", "."]) == ([(0, 4, ".")])
    assert day9.blocks_to_files([".", ".", 1, "."]) == (
        [(0, 2, "."), (2, 1, 1), (3, 1, ".")]
    )


def test_files_to_blocks():
    assert day9.files_to_blocks([(0, 1, 1), (1, 1, 2), (2, 1, 3)]) == [1, 2, 3]
    assert day9.files_to_blocks(([(0, 4, ".")])) == [".", ".", ".", "."]


def test_insert_file():
    assert day9.insert_file((2, 1, 3), (0, 4, ".")) == (
        (0, 1, 3),
        [(1, 3, "."), (2, 1, ".")],
    )
    assert day9.insert_file((99, 10, 1), (0, 4, ".")) == ((99, 10, 1), [(0, 4, ".")])


def test_find_space():
    blocks = day9.to_blocks("2333133121414131402")
    files = day9.blocks_to_files(blocks)
    assert day9.find_space(4, [(0, 4, ".")]) == (0, 4, ".")
    assert day9.find_space(3, [(0, 4, ".")]) == (0, 4, ".")
    assert day9.find_space(5, [(0, 4, ".")]) is None
    assert day9.find_space(3, files) == (2, 3, ".")


def test_per_file_compact():
    # fmt: off
    blocks = day9.to_blocks("2333133121414131402")
    files = day9.blocks_to_files(blocks)
    assert day9.per_file_compact(files) == [0, 0, 9, 9, 2, 1, 1, 1, 7, 7, 7, '.', 4, 4,
                                             '.', 3, 3, 3, '.', '.', '.', '.', 5, 5, 5, 5,
                                               '.', 6, 6, 6, 6, '.', '.', '.', '.', '.',
                                                 8, 8, 8, 8, '.', '.']


def test_part2():
    assert day9.part2("day9/input_example.txt") == 2858
    assert day9.part2("day9/input.txt") == 6321896265143
