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


def count_depth_increases(measurements):
    return len(measurements)


def test_count_depth_increases():
    assert count_depth_increases(exampleInput) == 7
