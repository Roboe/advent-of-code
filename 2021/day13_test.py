# https://adventofcode.com/2021/day/13


from collections import namedtuple

with open("day13.input.txt", "r") as f:
    input = f.read()

example_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


Dot = namedtuple("Dot", "x y")
Instruction = namedtuple("Instruction", "axis line")


def parse_input(raw_input):
    [raw_dots, raw_instructions] = raw_input.split("\n\n")

    dots = tuple(Dot(*map(int, point.split(","))) for point in raw_dots.splitlines())

    instructions = tuple(
        Instruction(instruction[11], int(instruction[13:]))
        for instruction in raw_instructions.splitlines()
    )

    return (dots, instructions)


def test_parse_input():
    assert parse_input(example_input) == (
        (
            Dot(6, 10),
            Dot(0, 14),
            Dot(9, 10),
            Dot(0, 3),
            Dot(10, 4),
            Dot(4, 11),
            Dot(6, 0),
            Dot(6, 12),
            Dot(4, 1),
            Dot(0, 13),
            Dot(10, 12),
            Dot(3, 4),
            Dot(3, 0),
            Dot(8, 4),
            Dot(1, 10),
            Dot(2, 14),
            Dot(8, 10),
            Dot(9, 0),
        ),
        (
            Instruction("y", 7),
            Instruction("x", 5),
        ),
    )


def fold_dot_by_line(dot, instruction):
    axis, line = instruction

    # fold up (horizontally)
    if axis == "y":
        return Dot(dot.x, line * 2 - dot.y) if dot.y > line else dot

    # fold left (vertically)
    elif axis == "x":
        return Dot(line * 2 - dot.x, dot.y) if dot.x > line else dot

    else:
        raise ValueError('Instruction axis should be "y" or "x"')


def count_dots_after_first_fold(dots, instructions):
    first_instruction = instructions[0]

    folded_dots = [
        fold_dot_by_line(dot, first_instruction)
        for dot in dots
        if dot._asdict()[first_instruction.axis] != first_instruction.line
    ]

    return len(set(folded_dots))


def test_count_dots_after_first_fold():
    assert count_dots_after_first_fold(*parse_input(example_input)) == 17

    # Solve AoC 13 part 1
    assert count_dots_after_first_fold(*parse_input(input)) == 687
