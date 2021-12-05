# https://adventofcode.com/2021/day/5

from collections import namedtuple
from math import copysign, trunc
from itertools import cycle

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


def trace_axis(start, end):
    step = trunc(copysign(1, end - start))
    path = range(start, end + step, step)

    return path


def trace_line(line):
    xs = trace_axis(line.a.x, line.b.x)
    ys = trace_axis(line.a.y, line.b.y)

    if len(xs) < len(ys):
        xs = cycle(xs)
    elif len(ys) < len(xs):
        ys = cycle(ys)

    traced_line = [Point(p[0], p[1]) for p in zip(xs, ys)]
    traced_line.sort()

    return traced_line


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
    # 0,0 -> 8,8
    assert trace_line(parse_line(example_input[8])) == [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
    ]
    # 8,0 -> 0,8
    assert trace_line(parse_line(example_input[1])) == [
        (0, 8),
        (1, 7),
        (2, 6),
        (3, 5),
        (4, 4),
        (5, 3),
        (6, 2),
        (7, 1),
        (8, 0),
    ]


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
