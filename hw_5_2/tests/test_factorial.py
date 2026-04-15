import pytest
from hw_5_2.src.functions import factorial

# Позитивные тесты и пограничные случаи
@pytest.mark.parametrize('n, expected', [
    # Позитивные
    (3, 6),         # 3! = 1 * 2 * 3
    (4, 24),        # Обычное целое число
    (5, 120),       # Обычное целое число
    (6, 720),       # Проверка на шаг больше
    (10, 3628800),  # Число побольше

    # Пограничные случаи
    (0, 1),         # Факториал 0 равен 1
    (1, 1),         # Факториал 1 равен 1
    (2, 2),         # Минимальный порог цикла
    (20, 2432902008176640000), # Большое число
])
def test_factorial_results(n, expected):
    assert factorial(n) == expected


# Негативные тесты
@pytest.mark.parametrize('n, exception', [
    # Отрицательные значения (ValueError)
    (-1, ValueError),
    (-10, ValueError),
    (-100, ValueError),

    # Неверные типы данных (TypeError)
    (3.5, TypeError),       # Float
    ("5", TypeError),       # String
    (None, TypeError),      # None
    ([5], TypeError),       # List
    ((5,), TypeError),      # Tuple
])
def test_factorial_errors(n, exception):
    with pytest.raises(exception):
        factorial(n)