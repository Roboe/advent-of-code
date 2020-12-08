# https://adventofcode.com/2020/day/8

with open("day08.input.txt", "r") as f:
    input = f.read().splitlines()


exampleInput = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()


def nop(argument, accumulator, i):
    return accumulator, i + 1


def acc(argument, accumulator, i):
    increment = int(argument)
    return accumulator + increment, i + 1


def jmp(argument, accumulator, i):
    leap = int(argument)
    return accumulator, i + leap


operations = {
    "nop": nop,
    "acc": acc,
    "jmp": jmp,
}


def loop(lines, accumulator=0, i=0, already=None):
    if already is None:
        already = [False for i in range(len(lines))]
    elif already[i] == True:
        return accumulator

    if i >= len(lines):
        return accumulator

    operation, argument = lines[i].split(" ")
    execute = operations[operation]

    already[i] = True
    next_accumulator, next_i = execute(argument, accumulator, i)
    return loop(lines, next_accumulator, next_i, already)


def test_nop():
    assert nop("+0", 0, 0) == (0, 1)
    assert nop("-99", 100, 50) == (100, 51)


def test_acc():
    assert acc("+0", 0, 0) == (0, 1)
    assert acc("-99", 100, 50) == (1, 51)


def test_jmp():
    assert jmp("+0", 0, 0) == (0, 0)
    assert jmp("+2", 100, 0) == (100, 2)
    assert jmp("-4", 100, 5) == (100, 1)


def test_value_before_infinite_loop():
    assert loop(exampleInput) == 5
    assert loop(input) == 1586
