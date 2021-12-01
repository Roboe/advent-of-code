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


def map_depth_increases(measurements):
    measurement_numbers = [int(raw_measurement) for raw_measurement in measurements]
    return [
        measurement_numbers[i] > measurement_numbers[i - 1]
        for i in range(len(measurements))
        if i > 0
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
    assert map_depth_increases(exampleInput) == [
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
    assert map_depth_increases(["986", "1001", "998"]) == [True, False]


def test_count_depth_increases():
    assert count_depth_increases(exampleInput) == 7
