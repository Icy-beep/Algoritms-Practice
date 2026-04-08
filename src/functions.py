import typing

IS_EVEN = lambda number: number % 2 == 0

def is_in_range(number):
    return number <= 2*10**4 and number >= -2*10**4

def sum_even_numbers(array: list[int]) -> int:
    total = 0

    for number in array:
        if not is_in_range(number):
            raise ValueError
        if IS_EVEN(number):
            total += number

    if total < 0:
        return 1

    return total