import pytest
from hw_5_2.src.functions import count_ones

# Позитивные тесты и пограничные случаи
@pytest.mark.parametrize('n, expected', [
    # Позитивные
    (3, 2),         # 3 в двоичной — 11 (две единицы)
    (4, 1),         # 4 в двоичной — 100 (одна единица)
    (7, 3),         # 7 в двоичной — 111
    (10, 2),        # 10 в двоичной — 1010
    (15, 4),        # 15 в двоичной — 1111
    (255, 8),       # 255 в двоичной — 11111111
    (1024, 1),      # Степени двойки всегда имеют одну единицу

    # Пограничные случаи
    (0, 0),         # 0 в двоичной — 0 (ноль единиц)
    (1, 1),         # 1 в двоичной — 1
    (2, 1),         # Минимальное четное
    (2**31 - 1, 31), # Максимальное значение для 32-бит
    (2**64, 1),     # Очень большое число
])
def test_count_ones_results(n, expected):
    assert count_ones(n) == expected


# Негативные тесты
@pytest.mark.parametrize('n, exception', [
    # Отрицательные значения (ValueError)
    (-1, ValueError),
    (-100, ValueError),

    # Неверные типы данных (TypeError)
    (3.0, TypeError),       # Float
    ("10", TypeError),      # String
    (None, TypeError),      # None
    ([7], TypeError),       # List
    ((1,), TypeError),      # Tuple
    ({"n": 5}, TypeError),  # Dict
    (True, TypeError),      # Bool
])
def test_count_ones_errors(n, exception):
    with pytest.raises(exception):
        count_ones(n)