import day6

import Guard


def test_guard_simple():
    obstructions = [(1, 1), (2, 0)]
    #   012
    # 0 ..#
    # 1 .#.

    bounds = {
        "x": 20,
        "y": 20,
    }

    # Initialize the guard
    guard = Guard.Guard(
        position=(0, 0), direction=(1, 0), obstructions=obstructions, bounds=bounds
    )

    # Test initial state
    assert guard.position == (0, 0), "Initial position is incorrect"
    assert guard.direction == (1, 0), "Initial direction is incorrect"
    assert guard.steps_count == 0, "Initial steps_count should be 0"
    assert guard.in_sight


def test_guard_no_obstructions():
    obstructions = []
    bounds = {"x": 10, "y": 1}

    guard = Guard.Guard(
        position=(0, 0), direction=(1, 0), obstructions=obstructions, bounds=bounds
    )

    assert guard.position == (0, 0), "Initial position is incorrect"
    assert guard.direction == (1, 0), "Initial direction is incorrect"
    assert guard.steps_count == 0, "Initial steps_count should be 0"
    assert guard.in_sight

    guard.step_forward()
    assert guard.position == (1, 0), "Position after first step is incorrect"
    assert guard.steps_count == 1, "Steps count after first step should be 1"
    assert guard.in_sight

    guard.step_forward()
    guard.step_forward()
    assert guard.position == (3, 0)

    guard.step_forward()
    guard.step_forward()
    guard.step_forward()
    guard.step_forward()
    guard.step_forward()
    guard.step_forward()
    guard.step_forward()
    guard.step_forward()
    guard.step_forward()
    assert not guard.in_sight
    assert guard.position == (10, 0)


def test_part1():
    assert day6.part1("day6/input_example.txt") == 41
    assert day6.part1("day6/input.txt") > 4987


def test_part2():
    assert day6.part2("day6/input_example.txt") == 6
    assert 1312 < day6.part2("day6/input.txt") < 1721
