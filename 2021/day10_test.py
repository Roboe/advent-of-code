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

ERROR_SCORING_TABLE = {
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

    score = sum(
        map(lambda character: ERROR_SCORING_TABLE[character], illegal_characters)
    )

    return score


def test_calculate_syntax_error_score():
    assert calculate_syntax_error_score(example_input) == 26397

    # Solve AoC 10 part 1
    assert calculate_syntax_error_score(input) == 442131


AUTOCOMPLETE_SCORING_TABLE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def autocomplete_brackets(line):
    openings = []
    for bracket in line:
        if bracket in OPENING_BRACKETS:
            openings.append(bracket)
        elif bracket == BRACKET_PAIRS[openings[-1]]:
            openings.pop()
        else:
            raise Error("Illegal character found")

    return "".join(map(lambda character: BRACKET_PAIRS[character], reversed(openings)))


def test_autocomplete_brackets():
    assert autocomplete_brackets("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"
    assert autocomplete_brackets("[(()[<>])]({[<{<<[]>>(") == ")}>]})"
    assert autocomplete_brackets("(((({<>}<{<{<>}{[]{[]{}") == "}}>}>))))"
    assert autocomplete_brackets("{<[[]]>}<{[{[{[]{()[[[]") == "]]}}]}]}>"
    assert autocomplete_brackets("<{([{{}}[<[[[<>{}]]]>[]]") == "])}>"


def calculate_completion_string_score(completion_string):
    total_score = 0
    for character in completion_string:
        character_score = AUTOCOMPLETE_SCORING_TABLE[character]
        total_score *= 5
        total_score += character_score

    return total_score


def test_calculate_completion_string_score():
    assert calculate_completion_string_score("}}]])})]") == 288957
    assert calculate_completion_string_score(")}>]})") == 5566
    assert calculate_completion_string_score("}}>}>))))") == 1480781
    assert calculate_completion_string_score("]]}}]}]}>") == 995444
    assert calculate_completion_string_score("])}>") == 294


def calculate_autocomplete_score(lines):
    completion_strings = [
        autocomplete_brackets(line)
        for line in lines
        if check_first_illegal_character(line) == None
    ]

    scores = list(map(calculate_completion_string_score, completion_strings))
    scores.sort()

    # NOTE it's assured there'll be an odd number of incomplete lines
    middle_score = scores[(len(scores) // 2)]

    return middle_score


def test_calculate_autocomplete_score():
    assert calculate_autocomplete_score(example_input) == 288957

    # Solve AoC 10 part 2
    assert calculate_autocomplete_score(input) == 3646451424
