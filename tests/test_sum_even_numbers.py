import pytest

from src.functions import sum_even_numbers

LIMIT = 20_000

# Positive scenarios
@pytest.mark.parametrize("array, expected", [
    ([2, 4, 6, 8], 20),
    ([1, 3, 5, 7], 0),
    ([2, -2, 4, -4], 0),
    ([10, 5, 2, 3], 12),
    ([], 0),
])
def test_positive_cases(array, expected):
    assert sum_even_numbers(array) == expected


# Negative scenarios
@pytest.mark.parametrize("array, expected", [
    ([-2, -4, -6], 1),
    ([-10, 2], 1),
    ([-2], 1),
    ([-100, 50, -20], 1),
    ([-2, -2, 4], 0),
    ('', TypeError),
    (1.2, TypeError),
    ([False, True], TypeError),
])
def test_negative_sum_rule(array, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            sum_even_numbers(array)
    else:
        assert sum_even_numbers(array) == expected


# Boundary scenarios
def test_boundary_exact_positive():
    """Number is 20_000"""
    assert sum_even_numbers([LIMIT]) == LIMIT

def test_boundary_exact_negative():
    """Number is -20_000"""
    assert sum_even_numbers([-LIMIT]) == 1

def test_boundary_overflow_positive():
    """Number is 20_002 out of limit ValueError must be called"""
    with pytest.raises(ValueError):
        sum_even_numbers([LIMIT + 2])

def test_boundary_overflow_negative():
    """Number is -20_002 out of limit ValueError must be called"""
    with pytest.raises(ValueError):
        sum_even_numbers([-LIMIT - 2])

def test_boundary_max_elements():
    """Тест на большое количество граничных данных (10^5 элементов)"""
    data = [2] * (10**5)
    data[-1] = 3
    assert sum_even_numbers(data) == 199_998