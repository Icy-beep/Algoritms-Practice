import pytest

from src.functions import frequent_element

LOWER_LIMIT = 1
UPPER_LIMIT = 2*10**4


# Positive scenarios
@pytest.mark.parametrize("array,expected", [
    ([1, 2, 2, 3], 2),                      # Стандартный случай
    ([5, 1, 2, 3, 4], 1),                   # Все элементы по разу
    ([10, 10, 5, 5, 1], 5),                 # Одинаковая частота, но один больше другого
    ([i for i in range(1, 1000)] * 2, 1),   # Большой массив
    ([1, 1, 1, 1, 1], 1),                   # Все элементы одинаковые
    ([1, 2, 3, 3], 3),                      # Лидер в конце списка
    ([4], 4),                               # Один элемент
])
def test_frequent_element_positive_cases(array, expected):
    assert frequent_element(array) == expected


# Boundary scenarios
@pytest.mark.parametrize("array,expected", [
    ([], 0),                                                            # Пустой список
    ([UPPER_LIMIT, UPPER_LIMIT, LOWER_LIMIT], UPPER_LIMIT),             # Верхний лимит в результате
    ([UPPER_LIMIT, LOWER_LIMIT], LOWER_LIMIT),                          # Два лимита одновременно
    ([LOWER_LIMIT, LOWER_LIMIT, UPPER_LIMIT, UPPER_LIMIT], LOWER_LIMIT),# Два лимита по краям списка
])
def test_frequent_element_boundary_cases(array, expected):
    assert frequent_element(array) == expected


# Negative scenarios
@pytest.mark.parametrize("array,expected", [
    ('', TypeError),                                      # Str вместо списка
    (False, TypeError),                                   # Bool вместо списка
    (True, TypeError),                                    # Bool вместо списка
    ([True, False, UPPER_LIMIT, LOWER_LIMIT], TypeError), # Bool в списке
    (3.5, TypeError),                                     # Float вместо списка
    (3, TypeError),                                       # Int вместо списка
    ([3.5, 4.5], TypeError),                              # Float в списке
    ([LOWER_LIMIT - 12, 1, 2], ValueError),               # За пределами нижнего лимита
    ([UPPER_LIMIT + 12, 1, 2], ValueError),               # За пределами верхнего лимита
])
def test_frequent_element_negative_cases(array, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            frequent_element(array)
    else:
        assert frequent_element(array) == expected
