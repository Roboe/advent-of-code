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
        (instruction[11], int(instruction[13:]))
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
