# https://adventofcode.com/2021/day/2

with open("day02.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()


def parse_line(line):
    instruction, raw_number = line.split(" ")
    return (instruction, int(raw_number))


def parse_commands(input):
    return list(map(parse_line, input))


def calculate_planned_course(commands, horizontal_position=0, depth=0):
    return (
        horizontal_position,
        depth,
    )


def calculate_planned_course_byproduct(commands):
    return 0


def test_parse_commands():
    assert parse_commands(example_input) == [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]


def test_calculate_planned_course():
    assert calculate_planned_course("") == (0, 0)
    assert calculate_planned_course(example_input) == (15, 10)


def test_planned_course_byproduct():
    assert calculate_planned_course_byproduct(example_input) == 150
