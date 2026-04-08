import time
import tracemalloc
from src.functions import sum_even_numbers

"""
Часть №1
Необходимо по поставленным задачам в примерах №1, №2 и №3, сформировать алгоритмы решения и записать на языке программирования Python.

Часть №2
Необходимо написать модульные тесты для разработанных алгоритмов, т.е. сформировать тестовые случаи и написать тестовые функции.
"""


def run_performance_test(data_size: int):
    print(f"--- Тестирование производительности ({data_size:,} элементов) ---")

    # 1. Подготовка данных (вне замера, чтобы не искажать результат)
    # Генерируем список четных чисел в рамках допустимого диапазона
    test_data = [20000] * data_size

    # 2. Замер времени выполнения
    start_time = time.perf_counter()
    result = sum_even_numbers(test_data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # 3. Замер потребления памяти (дополнительной)
    tracemalloc.start()
    # Выполняем еще раз для фиксации пиковой памяти именно внутри функции
    sum_even_numbers(test_data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # 4. Вывод результатов
    print(f"Результат суммы: {result}")
    print(f"Время выполнения: {execution_time:.4f} сек")
    print(f"Пиковое потребление памяти: {peak / 10 ** 6:.2f} MB")
    print("-" * 50)


if __name__ == "__main__":
    # Проверяем на 10^7 элементов
    run_performance_test(10 ** 7)