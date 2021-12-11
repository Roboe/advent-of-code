# https://adventofcode.com/2021/day/6

import itertools

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


def calculate_total_lanternfishes(lanternfishes, days=0):
    initial_lanternfishes_by_timer = {
        internal_timer: len(tuple(grouped_lanternfishes))
        for internal_timer, grouped_lanternfishes in itertools.groupby(
            sorted(lanternfishes)
        )
    }

    lanternfishes_by_timer = {
        timer: initial_lanternfishes_by_timer[timer]
        if timer in initial_lanternfishes_by_timer.keys()
        else 0
        for timer in range(0, 8 + 1)
    }

    for _ in range(0, days):
        newborns = to_be_reset = lanternfishes_by_timer[0]

        lanternfishes_by_timer = {
            (timer - 1): count
            for timer, count in lanternfishes_by_timer.items()
            if timer != 0
        }
        lanternfishes_by_timer[6] += to_be_reset
        lanternfishes_by_timer[8] = newborns

    return sum(lanternfishes_by_timer.values())


def test_lanternfish_cycle_optimized():
    assert calculate_total_lanternfishes(parse_input(example_input), 0) == 5
    assert calculate_total_lanternfishes(parse_input(example_input), 18) == 26
    assert calculate_total_lanternfishes(parse_input(example_input), 80) == 5934
    assert calculate_total_lanternfishes(parse_input(input), 80) == 390011
    assert calculate_total_lanternfishes(parse_input(example_input), 256) == 26984457539

    # Solve AoC part 2
    assert calculate_total_lanternfishes(parse_input(input), 256) == 1746710169834
