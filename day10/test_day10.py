import day10
import numpy as np

SIMPLE_ARRAY = np.arange(100).reshape(10, 10) % 10


def test_get_trailhead_locations():
    cropped_map, adjusted_start = day10.crop_map(
        SIMPLE_ARRAY, center=(0, 0), size=(3, 3)
    )
    assert day10.get_trailhead_locations(cropped_map) == [(0, 0), (1, 0)]


def test_build_graph():
    cropped_map, adjusted_start = day10.crop_map(
        SIMPLE_ARRAY, center=(0, 0), size=(3, 3)
    )
    assert day10.build_graph(array=cropped_map, start=adjusted_start) == {
        (0, 0): [(0, 1)],
        (0, 1): [],
    }


def test_part1():
    assert day10.part1(filepath="", array=SIMPLE_ARRAY) == 10
    assert day10.part1("day10/input_example.txt") == 36
    assert day10.part1("day10/input.txt") == 782
