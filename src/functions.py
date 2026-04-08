import typing
from itertools import count

IS_EVEN = lambda number: number % 2 == 0

def in_range(number, low, high):
    return low <= number <= high

def sum_even_numbers(array: list[int]) -> int:
    if not isinstance(array, list): raise TypeError()

    lower_limit = -2*10**4
    upper_limit = 2*10**4

    total = 0

    for number in array:
        if type(number) is bool:
            raise TypeError()
        if not in_range(number, lower_limit, upper_limit):
            raise ValueError()

        if IS_EVEN(number):
            total += number

    if total < 0:
        return 1

    return total


def frequent_element(array: list[int]) -> int:
    if not isinstance(array, list):  raise TypeError()
    if not array:  return 0

    lower_limit = 1
    upper_limit = 2*10**4
    counts = {}

    for number in array:
        if type(number) is not int:
            raise TypeError()
        if not in_range(number, lower_limit, upper_limit):
            raise ValueError()

        counts[number] = counts.get(number, 0) + 1

    max_frequency = 0
    leader = None

    for number, frequency in counts.items():
        if frequency > max_frequency:
            max_frequency = frequency
            leader = number

        elif frequency == max_frequency:
            if number < leader:
                leader = number

    return leader if leader is not None else 0
