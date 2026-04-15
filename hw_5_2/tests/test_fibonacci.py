import pytest
from hw_5_2.src.functions import fibonacci

# Позитивные тесты и пограничные случаи
@pytest.mark.parametrize('n, expected', [
    # Позитивные
    (2, [0, 1, 1]),            # F(2)
    (3, [0, 1, 1, 2]),         # F(3)
    (4, [0, 1, 1, 2, 3]),      # F(4)
    (5, [0, 1, 1, 2, 3, 5]),   # F(5)
    (6, [0, 1, 1, 2, 3, 5, 8]),# F(6)
    (7, [0, 1, 1, 2, 3, 5, 8, 13]), # F(7)
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]), # Длинная последовательность

    # Пограничные случаи
    (0, [0]),                  # (n=0)
    (1, [0, 1]),               # (n=1)
    (20, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]), # Большое n
])
def test_fibonacci_results(n, expected):
    assert fibonacci(n) == expected


# Негативные тесты
@pytest.mark.parametrize('n, exception', [
    # Отрицательные значения (ValueError)
    (-1, ValueError),
    (-5, ValueError),
    (-100, ValueError),

    # Неверные типы данных (TypeError)
    (2.0, TypeError),          # Float
    ("3", TypeError),          # String
    (None, TypeError),         # None
    ([], TypeError),           # List
    ({}, TypeError),           # Dict
    ((1,), TypeError),         # Tuple
])
def test_fibonacci_errors(n, exception):
    with pytest.raises(exception):
        fibonacci(n)