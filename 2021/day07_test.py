# https://adventofcode.com/2021/day/7

from statistics import median

with open("day07.input.txt", "r") as f:
    input = f.read()

example_input = """16,1,2,0,4,2,7,1,2,14"""


def parse_input(raw_input):
    return [int(raw_crab) for raw_crab in raw_input.split(",")]


def test_parse_input():
    assert parse_input(example_input) == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def calculate_cheapest_horizontal_position(crab_horizontal_positions):
    return median(crab_horizontal_positions)


def test_calculate_cheapest_horizontal_position():
    assert calculate_cheapest_horizontal_position(parse_input(example_input)) == 2


def calculate_minimal_fuel(crab_horizontal_positions):
    final_position = calculate_cheapest_horizontal_position(crab_horizontal_positions)
    total_fuel = 0
    for horizontal_position in crab_horizontal_positions:
        total_fuel += abs(horizontal_position - final_position)

    return int(total_fuel)


def test_calculate_minimal_fuel():
    assert calculate_minimal_fuel(parse_input(example_input)) == 37

    # Solve AoC 7 part 1
    assert calculate_minimal_fuel(parse_input(input)) == 343605
