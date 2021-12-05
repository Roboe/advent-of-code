# https://adventofcode.com/2021/day/5

import pytest
from collections import namedtuple

with open("day05.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()

Line = namedtuple("Line", "a b")
Point = namedtuple("Point", "x y")


def parse_line(raw_line_of_vent):
    [x1, y1, x2, y2] = [
        int(coord) for coord in raw_line_of_vent.replace(" -> ", ",").split(",")
    ]
    return Line(
        Point(x1, y1),
        Point(x2, y2),
    )


def test_parse_line():
    assert parse_line(example_input[0]) == ((0, 9), (5, 9))
    assert parse_line(example_input[1]) == ((8, 0), (0, 8))
    assert parse_line(example_input[2]) == ((9, 4), (3, 4))
    assert parse_line(example_input[3]) == ((2, 2), (2, 1))


def is_horizontal(line):
    return line.a.x == line.b.x


def is_vertical(line):
    return line.a.y == line.b.y


def exclude_diagonal_lines(lines_of_vent):
    return [line for line in lines_of_vent if is_horizontal(line) or is_vertical(line)]


def test_exclude_diagonal_lines():
    assert exclude_diagonal_lines(map(parse_line, example_input)) == [
        ((0, 9), (5, 9)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
    ]


def trace_line(line):
    if is_horizontal(line):
        return [
            Point(line.a.x, y)
            for y in range(min(line.a.y, line.b.y), max(line.a.y, line.b.y) + 1)
        ]
    elif is_vertical(line):
        return [
            Point(x, line.a.y)
            for x in range(min(line.a.x, line.b.x), max(line.a.x, line.b.x) + 1)
        ]
    else:
        raise NotImplementedError()


def test_trace_line():
    # 0,9 -> 5,9
    assert trace_line(parse_line(example_input[0])) == [
        (0, 9),
        (1, 9),
        (2, 9),
        (3, 9),
        (4, 9),
        (5, 9),
    ]
    # 9,4 -> 3,4
    assert trace_line(parse_line(example_input[2])) == [
        (3, 4),
        (4, 4),
        (5, 4),
        (6, 4),
        (7, 4),
        (8, 4),
        (9, 4),
    ]
    # 7,0 -> 7,4
    assert trace_line(parse_line(example_input[4])) == [
        (7, 0),
        (7, 1),
        (7, 2),
        (7, 3),
        (7, 4),
    ]
    # 2,2 -> 2,1
    assert trace_line(parse_line(example_input[3])) == [
        (2, 1),
        (2, 2),
    ]
    # 8,0 -> 0,8
    with pytest.raises(NotImplementedError):
        trace_line(parse_line(example_input[1]))


def determine_number_of_overlapping_points(lines_of_vents, include_diagonals=False):
    traced_lines = [
        set(trace_line(line))
        for line in exclude_diagonal_lines(map(parse_line, lines_of_vents))
    ]

    intersected_points = set()

    for curr_traced_line in traced_lines:
        for other_traced_line in traced_lines:
            if curr_traced_line == other_traced_line:
                continue

            intersection = curr_traced_line.intersection(other_traced_line)

            intersected_points.update(intersection)

    return len(intersected_points)


def test_determine_number_of_overlapping_points():
    assert determine_number_of_overlapping_points(example_input) == 5

    # Solve AoC 5 part 1
    assert determine_number_of_overlapping_points(input) == 5698

    assert (
        determine_number_of_overlapping_points(example_input, include_diagonals=True)
        == 12
    )
