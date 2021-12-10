# https://adventofcode.com/2021/day/10

from itertools import chain

with open("day10.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()


BRACKET_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
OPENING_BRACKETS = BRACKET_PAIRS.keys()
CLOSING_BRACKETS = BRACKET_PAIRS.values()

SCORING_TABLE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def check_first_illegal_character(line):
    illegal_character = None
    openings = []
    for bracket in line:
        if bracket in OPENING_BRACKETS:
            openings.append(bracket)
        elif bracket == BRACKET_PAIRS[openings[-1]]:
            openings.pop()
        else:
            illegal_character = bracket
            break

    return illegal_character


def test_check_first_illegal_character():
    assert check_first_illegal_character("[({(<(())[]>[[{[]{<()<>>") == None
    assert check_first_illegal_character("[(()[<>])]({[<{<<[]>>(") == None
    assert check_first_illegal_character("{([(<{}[<>[]}>{[]{[(<()>") == "}"
    assert check_first_illegal_character("[[<[([]))<([[{}[[()]]]") == ")"
    assert check_first_illegal_character("[{[{({}]{}}([{[{{{}}([]") == "]"
    assert check_first_illegal_character("[<(<(<(<{}))><([]([]()") == ")"
    assert check_first_illegal_character("<{([([[(<>()){}]>(<<{{") == ">"


def calculate_syntax_error_score(lines):
    illegal_characters = [
        illegal_character
        for illegal_character in map(check_first_illegal_character, lines)
        if illegal_character != None
    ]

    score = sum(map(lambda character: SCORING_TABLE[character], illegal_characters))

    return score


def test_calculate_syntax_error_score():
    assert calculate_syntax_error_score(example_input) == 26397

    # Solve AoC 10 part 1
    assert calculate_syntax_error_score(input) == 442131
