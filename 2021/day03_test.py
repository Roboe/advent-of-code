# https://adventofcode.com/2021/day/3

with open("day03.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()


def calculate_gamma_epsilon_rates(diagnostic_report):
    acc_weigths = [0 for _ in range(len(diagnostic_report[0]))]

    for binary_numbers in diagnostic_report:
        weights = [1 if binary_digit == "1" else -1 for binary_digit in binary_numbers]
        for index, weight in enumerate(weights):
            acc_weigths[index] += weight

    gamma_digits = ["1" if weight > 0 else "0" for weight in acc_weigths]
    epsilon_digits = ["0" if weight > 0 else "1" for weight in acc_weigths]
    binary_gamma = "".join(gamma_digits)
    binary_epsilon = "".join(epsilon_digits)

    return (int(binary_gamma, 2), int(binary_epsilon, 2))


def calculate_gamma_rate(diagnostic_report):
    (gamma_rate, _) = calculate_gamma_epsilon_rates(diagnostic_report)
    return gamma_rate


def calculate_epsilon_rate(diagnostic_report):
    (_, epsilon_rate) = calculate_gamma_epsilon_rates(diagnostic_report)
    return epsilon_rate


def calculate_power_consumption(diagnostic_report):
    (gamma_rate, epsilon_rate) = calculate_gamma_epsilon_rates(diagnostic_report)
    return gamma_rate * epsilon_rate


def test_calculate_gamma_rate():
    assert calculate_gamma_rate(example_input) == 22  # 10110


def test_calculate_epsilon_rate():
    assert calculate_epsilon_rate(example_input) == 9  # 01001


def test_calculate_power_consumption():
    assert calculate_power_consumption(example_input) == 198

    # Solve AoC 3 part 1
    assert calculate_power_consumption(input) == 841526


def calculate_oxygen_generator_rating(diagnostic_report):
    filtered_list = diagnostic_report

    for bit_index in range(len(diagnostic_report[0])):
        zeros = []
        ones = []

        for binary_numbers in filtered_list:
            bit = binary_numbers[bit_index]
            if bit == "0":
                zeros.append(binary_numbers)
            elif bit == "1":
                ones.append(binary_numbers)
            else:
                continue

        filtered_list = zeros if len(zeros) > len(ones) else ones

    return int(filtered_list[0], 2)


def calculate_co2_scrubber_rating(diagnostic_report):
    filtered_list = diagnostic_report

    for bit_index in range(len(diagnostic_report[0])):
        if len(filtered_list) == 1:
            break

        zeros = []
        ones = []

        for binary_numbers in filtered_list:
            bit = binary_numbers[bit_index]
            if bit == "0":
                zeros.append(binary_numbers)
            elif bit == "1":
                ones.append(binary_numbers)
            else:
                continue

        filtered_list = ones if len(zeros) > len(ones) else zeros

    return int(filtered_list[0], 2)


def calculate_life_support_rating(diagnostic_report):
    return calculate_oxygen_generator_rating(
        diagnostic_report
    ) * calculate_co2_scrubber_rating(diagnostic_report)


def test_calculate_oxygen_generator_rating():
    assert calculate_oxygen_generator_rating(example_input) == 23  # 10111


def test_calculate_co2_scrubber_rating():
    assert calculate_co2_scrubber_rating(example_input) == 10  # 01010


def test_calculate_life_support_rating():
    assert calculate_life_support_rating(example_input) == 230

    # Solve AoC 3 part 2
    assert calculate_life_support_rating(input) == 4790390
