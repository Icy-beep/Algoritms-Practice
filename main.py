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


def run_performance_test_1(data_size: int):
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


def run_performance_test_2(data_size: int):
    print(f"--- Тестирование производительности ({data_size:,} элементов) ---")

    # 1. Замер производительности (время)
    # Генерируем данные заранее ОДИН раз, чтобы замерить только работу функции
    test_data = [random.randint(1, 20000) for _ in range(data_size)]

    start_time = time.perf_counter()
    result = frequent_element(test_data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # 2. Замер потребления памяти (честный)
    tracemalloc.start()

    # Чтобы увидеть РЕАЛЬНЫЙ пик, мы должны создать данные И
    # запустить функцию внутри одного сеанса tracemalloc
    internal_data = [random.randint(1, 20000) for _ in range(data_size)]
    frequent_element(internal_data)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Освобождаем память для чистоты
    del internal_data

    # 3. Вывод результатов
    print(f"Результат (лидер): {result}")
    print(f"Время выполнения алгоритма: {execution_time:.4f} сек")
    print(f"Пиковое потребление (данные + словарь): {peak / 10 ** 6:.2f} MB")
    print("-" * 55)


if __name__ == "__main__":
    run_performance_test_1(10 ** 7)
    run_performance_test_2(10 ** 7)