# https://adventofcode.com/2021/day/3

with open("day03.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()


def calculate_gamma_rate(diagnostic_report):
    return 0


def calculate_power_consumption(diagnostic_report):
    return 0


def test_calculate_gamma_rate():
    assert calculate_gamma_rate(example_input) == 22  # 10110


def test_calculate_power_consumption():
    assert calculate_power_consumption(example_input) == 198
