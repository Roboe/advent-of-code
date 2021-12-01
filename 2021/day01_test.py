# https://adventofcode.com/2021/day/1

with open("day01.input.txt", "r") as f:
    input = f.read().splitlines()

exampleInput = """199
200
208
210
200
207
240
269
260
263""".splitlines()

example_part2_grouping_by_three = [607, 618, 618, 617, 647, 716, 769, 792]


def parse_measurements(raw_measurements):
    measurement = [int(raw_measurement) for raw_measurement in raw_measurements]
    return measurement


def group_measures_by_three(measurements):
    return [
        measurements[i - 2] + measurements[i - 1] + measurements[i]
        for i in range(len(measurements))
        if i > 1
    ]


def map_depth_increases(measurements):
    return [
        measurements[i] > measurements[i - 1] for i in range(len(measurements)) if i > 0
    ]


def count_depth_increases(measurements):
    return len(
        [
            does_increase
            for does_increase in map_depth_increases(measurements)
            if does_increase == True
        ]
    )


def test_check_depth_increases():
    assert map_depth_increases(parse_measurements(exampleInput)) == [
        # (N/A - no previous measurement)
        True,  # 200 (increased)
        True,  # 208 (increased)
        True,  # 210 (increased)
        False,  # 200 (decreased)
        True,  # 207 (increased)
        True,  # 240 (increased)
        True,  # 269 (increased)
        False,  # 260 (decreased)
        True,  # 263 (increased)
    ]
    assert map_depth_increases(parse_measurements(["986", "1001", "998"])) == [
        True,
        False,
    ]
    assert map_depth_increases(example_part2_grouping_by_three) == [
        # A: 607 (N/A - no previous sum)
        True,  # B: 618 (increased)
        False,  # C: 618 (no change)
        False,  # D: 617 (decreased)
        True,  # E: 647 (increased)
        True,  # F: 716 (increased)
        True,  # G: 769 (increased)
        True,  # H: 792 (increased)
    ]


def test_count_depth_increases():
    assert count_depth_increases(parse_measurements(exampleInput)) == 7
    assert count_depth_increases(example_part2_grouping_by_three) == 5


def test_solve_aoc_1_part_1():
    assert count_depth_increases(parse_measurements(input)) == 1228


def test_group_by_three():
    assert (
        group_measures_by_three(parse_measurements(exampleInput))
        == example_part2_grouping_by_three
    )
