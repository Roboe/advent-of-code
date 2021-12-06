# https://adventofcode.com/2021/day/6

with open("day06.input.txt", "r") as f:
    input = f.read()

example_input = """3,4,3,1,2"""


def parse_input(raw_input):
    return [int(raw_lanternfish) for raw_lanternfish in (raw_input).split(",")]


def test_parse_input():
    assert parse_input(example_input) == [3, 4, 3, 1, 2]


def lanternfish_cycle(lanternfishes, days=0):
    if days == 0:
        return lanternfishes

    next_lanternfishes = []
    births_count = 0
    for lanternfish in lanternfishes:
        next_lanternfish = lanternfish
        if lanternfish == 0:
            next_lanternfish = 6
            births_count += 1
        else:
            next_lanternfish -= 1

        next_lanternfishes.append(next_lanternfish)

    newborn_lanternfishes = [8] * births_count
    return lanternfish_cycle(
        next_lanternfishes + newborn_lanternfishes,
        days - 1,
    )


def test_lanternfish_cycle():
    assert len(lanternfish_cycle(parse_input(example_input), 0)) == 5
    assert len(lanternfish_cycle(parse_input(example_input), 18)) == 26
    assert len(lanternfish_cycle(parse_input(example_input), 80)) == 5934

    # Solve AoC 6 part 1
    assert len(lanternfish_cycle(parse_input(input), 80)) == 390011
