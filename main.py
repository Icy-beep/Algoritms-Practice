import time
import tracemalloc
import random
from src.functions import sum_even_numbers, frequent_element

"""
Часть №1
Необходимо по поставленным задачам в примерах №1, №2 и №3, сформировать алгоритмы решения и записать на языке программирования Python.

Часть №2
Необходимо написать модульные тесты для разработанных алгоритмов, т.е. сформировать тестовые случаи и написать тестовые функции.
"""


def run_performance_test(func, data_gen_func, label):
    print(f"--- Тестирование: {label} ---")

    # 1. Готовим данные заранее (чтобы генерация не входила в замер времени)
    test_data = data_gen_func()
    size_mb = len(test_data) * 8 / 10 ** 6  # Примерный вес указателей в списке
    print(f"Размер входного списка: {len(test_data):,} элементов (~{size_mb:.1f} MB)")

    # 2. Замер чистого времени выполнения
    start_time = time.perf_counter()
    result = func(test_data)
    execution_time = time.perf_counter() - start_time

    # 3. Замер пикового потребления памяти ВНУТРИ функции
    # (Мы не включаем сам test_data в пик, так как он уже в памяти)
    tracemalloc.start()
    func(test_data)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Результат: {result}")
    print(f"Время выполнения: {execution_time:.4f} сек")
    print(f"Доп. память (пик внутри функции): {peak / 10 ** 6:.2f} MB")
    print("-" * 50)

    del test_data  # Очистка для следующего теста


if __name__ == "__main__":
    DATA_SIZE = 10 ** 7

    # Тест 1: Сумма четных
    run_performance_test(
        sum_even_numbers,
        lambda: [20000] * DATA_SIZE,
        "sum_even_numbers"
    )

    # Тест 2: Самый частый элемент
    run_performance_test(
        frequent_element,
        lambda: [random.randint(1, 20000) for _ in range(DATA_SIZE)],
        "frequent_element"
    )