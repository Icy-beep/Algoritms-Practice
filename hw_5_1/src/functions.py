IS_EVEN = lambda number: number % 2 == 0

def sum_even_numbers(array: list[int]) -> int:
    if not isinstance(array, list): raise TypeError()

    total = 0

    for number in array:
        if type(number) is bool:
            raise TypeError()

        if IS_EVEN(number):
            total += number

    if total < 0:
        return 1

    return total


def frequent_element(array: list[int]) -> int:
    if not isinstance(array, list):  raise TypeError()
    if not array:  return 0

    counts = {}

    for number in array:
        if type(number) is not int:
            raise TypeError()

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

'''

Проблема:
    Дан массив целых чисел `nums` и целое число `target`, 
        вернуть индексы двух чисел, так чтобы их сумма была равна `target`.
        
Для каждого набора входных данных существует одно решение, 
    также вы не можете использовать один элемент дважды. 
    
Ответ можно вернуть в любом порядке.

Пример №1

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
Пример №2

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
Ограничения:

    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    
'''
def two_sum(nums: list[int], target: int) -> None | list[int]:
    if not isinstance(nums, list):  raise TypeError()
    if not isinstance(target, int): raise TypeError()

    if len(nums) < 2:  return None

    for i in range(len(nums)):
        if not isinstance(nums[i], int):  raise TypeError()
        for j in range(i + 1, len(nums)):
            if not isinstance(nums[j], int):  raise TypeError()
            if nums[i] + nums[j] == target:
                return [i, j]

    return None