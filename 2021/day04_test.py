# https://adventofcode.com/2021/day/4

from itertools import chain

with open("day04.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".splitlines()


def parse_board(raw_board):
    return tuple(
        [
            tuple(map(int, raw_numbers))
            for raw_numbers in map(lambda raw_line: raw_line.strip().split(), raw_board)
        ]
    )


def parse_input(input):
    # first line
    order = [int(raw_number) for raw_number in input[0].split(",")]

    # from third line
    boards = [
        parse_board(input[index : index + 5]) for index in range(2, len(input), 6)
    ]

    return (order, boards)


def test_parse_input():
    assert parse_input(example_input) == (
        [
            7,
            4,
            9,
            5,
            11,
            17,
            23,
            2,
            0,
            14,
            21,
            24,
            10,
            16,
            13,
            6,
            15,
            25,
            12,
            22,
            18,
            20,
            8,
            19,
            3,
            26,
            1,
        ],
        [
            (
                (22, 13, 17, 11, 0),
                (8, 2, 23, 4, 24),
                (21, 9, 14, 16, 7),
                (6, 10, 3, 18, 5),
                (1, 12, 20, 15, 19),
            ),
            (
                (3, 15, 0, 2, 22),
                (9, 18, 13, 17, 5),
                (19, 8, 7, 25, 23),
                (20, 11, 10, 24, 4),
                (14, 21, 16, 12, 6),
            ),
            (
                (14, 21, 17, 24, 4),
                (10, 16, 15, 9, 19),
                (18, 8, 23, 26, 20),
                (22, 11, 13, 6, 5),
                (2, 0, 12, 3, 7),
            ),
        ],
    )


def transpose(board):
    return tuple(zip(*board))


def test_transpose():
    assert transpose(
        (
            (22, 13, 17, 11, 0),
            (8, 2, 23, 4, 24),
            (21, 9, 14, 16, 7),
            (6, 10, 3, 18, 5),
            (1, 12, 20, 15, 19),
        )
    ) == (
        (22, 8, 21, 6, 1),
        (13, 2, 9, 10, 12),
        (17, 23, 14, 3, 20),
        (11, 4, 16, 18, 15),
        (0, 24, 7, 5, 19),
    )


def check_has_a_complete_line(board, drawn_numbers):
    drawn_numbers = set(drawn_numbers)
    lines = board + transpose(board)

    return any(
        map(
            lambda line: all(
                map(
                    lambda number: number in drawn_numbers,
                    line,
                ),
            ),
            lines,
        ),
    )


def calculate_score(board, rounds):
    sum_of_all_unmarked_numbers = sum(
        filter(
            lambda number: number not in rounds,
            chain(*board),
        )
    )
    last_called_number = rounds[-1]

    return sum_of_all_unmarked_numbers * last_called_number


def find_winning_board_score(raw_input):
    order, boards = parse_input(raw_input)

    first_winner_board = None
    rounds_until_winner = None
    for round in range(1, len(order)):
        winner_boards = filter(
            lambda board: check_has_a_complete_line(board, order[:round]),
            boards,
        )
        winner_board = next(winner_boards, None)

        if winner_board != None:
            first_winner_board = winner_board
            rounds_until_winner = order[:round]
            break

    return calculate_score(first_winner_board, rounds_until_winner)


def test_find_winning_board_score():
    assert find_winning_board_score(example_input) == 4512

    # Solve AoC 4 part 1
    assert find_winning_board_score(input) == None
