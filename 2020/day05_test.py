# https://adventofcode.com/2020/day/5

with open("day05.input.txt", "r") as f:
    input = f.read().splitlines()


def bsp(directions, min=0, max=0):
    if max == min:
        return min

    if len(directions) == 0:
        return min, max

    direction, *next_directions = directions
    half = (max - min) // 2 + min

    if direction == "F" or direction == "L":
        return bsp(next_directions, min, half)
    elif direction == "B" or direction == "R":
        return bsp(next_directions, 1 + half, max)


def bsp_row(directions):
    return bsp(directions, min=0, max=127)


def bsp_col(directions):
    return bsp(directions, min=0, max=7)


def find_seat(directions):
    return bsp_row(directions[:7]), bsp_col(directions[7:])


def calc_seat_id(seat):
    row, col = seat
    return row * 8 + col


def find_seat_id(directions):
    return calc_seat_id(find_seat(directions))


def calc_all_seat_ids(directions):
    return [find_seat_id(direction) for direction in directions]


def find_highest_seat_id(directions):
    return max(calc_all_seat_ids(directions))


def find_hole_in_range(range):
    current, *next_range = range
    hole = current + 1
    return hole if hole != next_range[0] else find_hole_in_range(next_range)


def find_missing_seat_id(directions):
    sorted_seat_ids = sorted(calc_all_seat_ids(directions))
    return find_hole_in_range(sorted_seat_ids)


def test_find_correct_row():
    assert bsp_row("F") == (0, 63)
    assert bsp_row("FB") == (32, 63)
    assert bsp_row("FBF") == (32, 47)
    assert bsp_row("FBFB") == (40, 47)
    assert bsp_row("FBFBB") == (44, 47)
    assert bsp_row("FBFBBF") == (44, 45)
    assert bsp_row("FBFBBFF") == 44


def test_find_correct_col():
    assert bsp_col("RLR") == 5


def test_find_correct_seat():
    assert find_seat("FBFBBFFRLR") == (44, 5)
    assert find_seat("BFFFBBFRRR") == (70, 7)
    assert find_seat("FFFBBBFRRR") == (14, 7)
    assert find_seat("BBFFBBFRLL") == (102, 4)


def test_find_correct_seat_id():
    assert find_seat_id("FBFBBFFRLR") == 357
    assert find_seat_id("BFFFBBFRRR") == 567
    assert find_seat_id("FFFBBBFRRR") == 119
    assert find_seat_id("BBFFBBFRLL") == 820


def test_solve_aoc_5_part_1():
    assert find_highest_seat_id(input) == 883


def test_solve_aoc_5_part_2():
    assert find_missing_seat_id(input) == 532
