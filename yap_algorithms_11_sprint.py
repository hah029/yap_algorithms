from typing import List, Tuple, Optional
import sys
import time, random

# ===============================================================================================
# region Примеры из теории

# region Вариант нахождения скользящего среднего для временного ряда
# (наивный алгоритм) - из теории
# def moving_average(timeseries, K):
#     result = []  # Пустой список.
#     for begin_index in range(0, len(timeseries) - K + 1):
#         end_index = begin_index + K
#         # Просматриваем окно шириной K.
#         current_sum = 0
#         for v in timeseries[begin_index:end_index]:
#             current_sum += v
#         current_avg = current_sum / K
#         result.append(current_avg)
#     return result
# endregion
# region Оптимизированный вариант нахождения скользящего среднего для
# временного ряда
# def moving_average(timeseries, K):
#     result = []  # Пустой массив.
#     # Первый раз вычисляем значение честно и сохраняем результат.
#     current_sum = sum(timeseries[0:K])
#     result.append(current_sum / K)
#     for i in range(0, len(timeseries) - K):
#         current_sum -= timeseries[i]
#         current_sum += timeseries[i+K]
#         current_avg = current_sum / K
#         result.append(current_avg)
#     return result
# endregion
# region Алгоритм для фитнес-тренажёра
# def twosum(numbers, X):
#     for i in range(0, len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] == X:
#                 return numbers[i], numbers[j]
#     # По условию задачи пара обязательно должна найтись.
#     # Но предусмотрительность не помешает:
#     # если пара не найдена - вернём None, None
#     # (или можно выкинуть exception).
#     return None, None
# endregion
# region Алгоритм для фитнес-тренажёра (1й вариант оптимизации)
# def twosum_with_sort(numbers, X):
#     # Сортируем исходный массив стандартной функцией.
#     numbers.sort()
#     left = 0
#     right = len(numbers) - 1
#     while left < right:
#         current_sum = numbers[left] + numbers[right]
#         if current_sum == X:
#             return numbers[left], numbers[right]
#         if current_sum < X:
#             left += 1
#         else:
#             right -= 1
#     # Если ничего не нашлось в цикле,
#     # значит, нужной пары элементов в массиве нет.
#     return None, None
# endregion
# region Алгоритм для фитнес-тренажёра (2й вариант оптимизации)
# def twosum_extra_ds(numbers, X):
#     # Создаём вспомогательную структуру данных с быстрым поиском элемента.
#     previous = set()

#     for A in numbers:
#         Y = X - A
#         if Y in previous:
#             return A, Y
#         else:
#             previous.add(A)

#     # Если ничего не нашлось в цикле, значит,
#     # нужной пары элементов в массиве нет.
#     return None, None
# endregion
# region Линейный поиск (наивный алгоритм)
# def find_element(numbers, x):
#     for i in range(len(numbers)): # проходим по всем элементам массива
#         if numbers[i] == x: # сравниваем их с иксом
#             return i  # если нашли - возвращаем индекс
#     return -1  # если не нашли - возвращаем -1
# endregion
# region Алгоритм, который ничего не делает, но считает время выполнения
# import time
# time_start = time.time()
# i = 0
# while i < 1000000000:
#     # Do nothing
#     i += 1
# time_finish = time.time()
# time_span = time_finish - time_start
# print(time_span, 'seconds')
# endregion
# region Алгоритмы считывания данных из потока ввода
# import sys
# def main():
#     num_lines = int(input())  # Считываем первую строку из потока ввода
#     output_numbers = []
#     for i in range(num_lines):
#         # Лучше использовать именно sys.stdin.readline() вместо input()
#         line = sys.stdin.readline().rstrip()
#         value_1, value_2 = line.split()
#         value_1 = int(value_1)
#         value_2 = int(value_2)
#         result = value_1 + value_2
#         output_numbers.append(str(result))
#     print('\n'.join(output_numbers))
# if __name__ == '__main__':
#     main()
# endregion
# region Алгоритм определения простоты числа (наивный)
# def is_prime(n):
#     if n == 1:
#         return False
#     i = 2
#     while i < n:                  # проверяем от 2 до n
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True
# endregion
# region 2й вариант алгоритма определения простоты числа (наивный)
# def is_prime(n):
#     if n == 1:
#         return False
#     i = 2
#     while i * i <= n:           # проверяем от 2 до sqrt(n)
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True
# endregion
# region Алгоритм, определяющий все простые числа до n
# (с помощью функции is_prime())
# def get_smaller_primes(n):
#     smaller_primes = []
#     for num in range(2, n + 1):
#         if is_prime(num):
#             smaller_primes.append(num)
#     return smaller_primes
# endregion
# region Решето Эратосфена (обычный вариант)
# def eratosthenes(n):
#     numbers = list(range(n + 1))
#     numbers[0] = numbers[1] = False
#     for num in range(2, n):
#         if numbers[num]:
#             for j in range(2 * num, n + 1, num):
#                 numbers[j] = False
#     return numbers
# endregion
# region Решето Эратосфена (более эффективный вариант)
# def eratosthenes_effective(n):
#     numbers = list(range(n + 1))
#     numbers[0] = numbers[1] = False
#     for num in range(2, n):
#         if numbers[num]:
#             for j in range(num * num, n + 1, num):
#                 numbers[j] = False
#     return numbers
# endregion
# region Алгоритм поиска простых чисел в последовательности,
# работающий за линейное время
# def get_least_primes_linear(n):
#     lp = [0] * (n + 1)
#     primes = []
#     for i in range(2, n + 1):
#         if lp[i] == 0:
#             lp[i] = i
#             primes.append(i)
#         for p in primes:
#             x = p * i
#             if (p > lp[i]) or (x > n):
#                 break
#             lp[x] = p
#     return primes, lp
# print(get_least_primes_linear(100))
# endregion

# endregion
# ===============================================================================================

# ===============================================================================================
# region Задачи Яндекс-контест

# Блок 1.
# region Задача A: A + B (решено)
# def get_sum(a: int, b: int) -> int:
#     return a + b
# def read_input() -> Tuple[int, int]:
#     a = int(input())
#     b = int(input())
#     return a, b
# a, b = read_input()
# print(get_sum(a, b))
# endregion
# region Задача B: Застежка-молния (решено)
# def zipper(a: List[int], b: List[int]) -> List[int]:
#     res = []
#     for i in range(len(a)):
#         res.append(a[i])
#         res.append(b[i])
#     return res
# def read_input() -> Tuple[List[int], List[int]]:
#     n = int(input())
#     a = list(map(int, input().strip().split()))
#     b = list(map(int, input().strip().split()))
#     return a, b
# a, b = read_input()
# print(" ".join(map(str, zipper(a, b))))
# endregion
# region Задача C: Скользящее среднее (решено)
# def moving_average(arr: List[int], window_size: int) -> List[float]:
#     result = []
#     current_sum = sum(arr[0:window_size])
#     result.append(current_sum / window_size)
#     for i in range(0, len(arr) - window_size):
#         current_sum = current_sum - arr[i]
#         current_sum = current_sum + arr[window_size + i]
#         result.append(current_sum / window_size)
#     return result
# def read_input() -> Tuple[List[int], int]:
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     window_size = int(input())
#     return arr, window_size
# arr, window_size = read_input()
# print(" ".join(map(str, moving_average(arr, window_size))))
# endregion
# region Задача D: Две фишки (решено)
# def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target_sum:
#                 return (arr[i], arr[j])
#     return None
# def read_input() -> Tuple[List[int], int]:
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     target_sum = int(input())
#     return arr, target_sum
# def print_result(result: Optional[Tuple[int, int]]) -> None:
#     if result is None:
#         print(None)
#     else:
#         print(" ".join(map(str, result)))
# arr, target_sum = read_input()
# print_result(two_sum(arr, target_sum))
# endregion
# region Задача E: Две фишки-2 (решено)
# def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
#     arr.sort()
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_sum:
#             return arr[left], arr[right]
#         if current_sum > target_sum:
#             right -= 1
#         else:
#             left += 1
#     return None
# def read_input() -> Tuple[List[int], int]:
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     target_sum = int(input())
#     return arr, target_sum
# def print_result(result: Optional[Tuple[int, int]]) -> None:
#     if result is None:
#         print(None)
#     else:
#         print(" ".join(map(str, result)))
# arr, target_sum = read_input()
# print_result(two_sum(arr, target_sum))
# endregion

# Блок 2.
# region Задача А: Значение функции (решено)
# def read_input() -> Tuple:
#     line = tuple(map(int, input().strip().split()))
#     return line
# def get_function_result(a: int, x: int, b: int, c: int) -> float:
#     return a * x * x + b * x + c
# a, x, b, c = read_input()
# print(get_function_result(a, x, b, c))
# endregion
# region Задача B: Четные и нечетные числа (решено)
# def read_input() -> Tuple:
#     line = tuple(map(int, input().strip().split()))
#     return line
# def check_odd_or_even(a: int, b: int, c: int) -> str:
#     if ((a % 2 == 0 and b % 2 == 0 and c % 2 == 0)
#          or (a % 2 != 0 and b % 2 != 0 and c % 2 != 0)):
#         return 'WIN'
#     return 'FAIL'
# a, b, c = read_input()
# print(check_odd_or_even(a, b, c))
# endregion
# region Задача C: Соседи
# def read_input() -> List:
#     row_count = int(input())
#     col_count = int(input())
#     tbl = []
#     for i in range(row_count):
#         row = list(map(int, input().strip().split()))
#         tbl.append(row)
#     x_row = int(input())
#     x_col = int(input())
#     return x_row, x_col, tbl
# def get_neighbors(x: int, y: int, matrix: List) -> List:
#     directions = [
#         [-1, 0],
#         [0, 1],
#         [1, 0],
#         [0, -1],
#     ]
#     neighbors = []
#     for direction in directions:
#         if ((x + direction[0] < 0 or x + direction[0] > len(matrix) - 1) or
#             (y + direction[1] < 0 or y + direction[1] > len(matrix[0]) - 1)):
#             continue
#         neighbors.append(matrix[x + direction[0]][y + direction[1]])
#     neighbors.sort()
#     return neighbors
# row, col, table = read_input()
# print(" ".join(map(str, get_neighbors(row, col, table))))
# endregion
# region Задача D: Хаотичность погоды
# def read_input() -> List:
#     chaos_check_periods = int(input())
#     temperature_sequence = list(map(int, input().strip().split()))
#     return chaos_check_periods, temperature_sequence
# def get_chaos_rating(n: int, seq: List) -> int:
#     if n == 1:
#         return 1
#     chaos_rating = 0
#     for i in range(n):
#         if i == 0:
#             less = seq[i] - 1
#         else:
#             less = seq[i - 1]
#         if i == n - 1:
#             more = seq[i] - 1
#         else:
#             more = seq[i + 1]
#         if seq[i] > less and seq[i] > more:
#             chaos_rating += 1
#     return chaos_rating
# chaos_check_periods, temperature_sequence = read_input()
# print(get_chaos_rating(chaos_check_periods, temperature_sequence))
# endregion
# region Задача E: Самое длинное слово
# def read_input() -> List:
#     text_len = int(input())
#     words = list(input().strip().split())
#     return words
# def get_longest_word(words: List) -> int:
#     max_len = 0
#     max_word = ''
#     for word in words:
#         if len(word) > max_len:
#             max_len = len(word)
#             max_word = word
#     return max_word, max_len
# # words = read_input()
# print("\n".join(map(str, get_longest_word(read_input()))))
# endregion
# region Задача F: Палиндром
# def read_input() -> str:
#     text = input()
#     return text.translate( { ord(i): None for i in ',.:; '} ).lower()
# def check_palindrome(text: str) -> int:
#     if text == text[::-1]:
#         return True
#     return False
# text = read_input()
# print(check_palindrome(text))
# endregion
# region Задача G: Работа из дома
# def read_input() -> int:
# 	value = int(input())
# 	return value
# def convert_decimal_to_binary(val: int) -> int:
# 	if val == 0:
# 		return 0
# 	res = []
# 	while val != 0:
# 		extra = val % 2
# 		val = val // 2
# 		res.append(extra)
# 	return ''.join(map(str, res[::-1]))
# value = read_input()
# print(convert_decimal_to_binary(value))
# endregion
# region Задача H: Двоичная система
# def read_input() -> List:
#     value_1 = [*map(int, input())]
#     value_2 = [*map(int, input())]
#     return value_1, value_2
# def get_binary_sum(num1: List[int], num2: List[int]) -> str:
#     num1 = num1[::-1]
#     num2 = num2[::-1]
#     num1_digit = len(num1)
#     num2_digit = len(num2)
#     max_digit = max(num1_digit, num2_digit)
#     num1 += [0] * (max_digit - num1_digit)
#     num2 += [0] * (max_digit - num2_digit)
#     overflow = 0
#     res = []
#     for obj in zip(num1, num2):
#         value = obj[0] + obj[1] + overflow
#         overflow = value // 2
#         res.append(value % 2)
#     if overflow == 1:
#         res.append(1)
#     res = res[::-1]
#     return ''.join(map(str, res))
# value_1, value_2 = read_input()
# print(get_binary_sum(value_1, value_2))
# endregion
# region Задача I: Степень четырех
# def read_input() -> int:
#     return int(input())
# def solver(num: int) -> bool:
#     degrees = [1, 4, 16, 64, 256, 1024, 4096]
#     if num in degrees:
#         return True
#     return False
# num = read_input()
# print(solver(num))
# endregion
# region Задача J: Факторизация
# def read_input() -> int:
#     return int(input())
# def solver(num: int) -> List[int]:
#     res = []
#     delimiter = 2
#     while delimiter * delimiter <= num:
#         if num % delimiter == 0:
#             res.append(delimiter)
#             num //= delimiter
#         else:
#             delimiter += 1
#     if num > 1:
#         res.append(num)
#     return res
# num = read_input()
# print(' '.join(map(str, solver(num))))
# endregion
# region Задача K: Списочная форма
# def read_input() -> List:
#     size = int(input())
#     num1 = list(map(int, input().strip().split()))
#     num2 = int(input())
#     return num1, num2
# def solver(num1: List[int], num2: int) -> List[int]:
#     num1 = num1[::-1]
#     res = 0
#     for i in range(len(num1)):
#         res += num1[i] * (10 ** i)
#     res += num2
#     return [*str(res)]
# num1, num2 = read_input()
# print(' '.join(map(str, solver(num1, num2))))
# endregion
# region Задача L: Лишняя буква
# def read_input() -> List[str]:
#     str1 = input()
#     str2 = input()
#     return str1, str2
# def solver(str1: str, str2: str) -> str:
#     str1 = [*str1]
#     str1.sort()
#     str2 = [*str2]
#     str2.sort()
#     for i in range(len(str2)):
#         if i == len(str2) - 1 or str1[i] != str2[i]:
#             return str2[i]
# str1, str2 = read_input()
# print(solver(str1, str2))
# endregion


# endregion
# ===============================================================================================

# ===============================================================================================
# region Финальные задания (тоже Яндекс-контест)

# region Задача A: Ближайший ноль (id=84157187)
# def read_input() -> List[int]:
#     count = int(input())
#     houses = list(map(int, sys.stdin.readline().rstrip().split()))
#     return count, houses
# def get_closest_house(houses: List[int]) -> List[int]:
#     output = [0] * len(houses)
#     zeroes = [
#         index for index, value in enumerate(houses) if value == 0
#     ]
#     for k in range(zeroes[0]):
#         output[k] = zeroes[0] - k
#     for k in range(len(zeroes) - 1): 
#         for pos in range(zeroes[k] + 1, zeroes[k + 1]):
#             output[pos] = min(pos - zeroes[k], zeroes[k + 1] - pos)
#     for k in range(zeroes[-1] + 1, len(houses)):
#         output[k] = k - zeroes[-1]
#     return output
# count, houses = read_input()
# print(' '.join(map(str, get_closest_house(houses))))
# endregion
# region Задача B: Ловкость рук (id=84158976)
# def read_input() -> List:
#     k = int(input())
#     tbl = []
#     for i in range(4):
#         row = [*input()]
#         tbl.append(row)
#     return k, tbl
# def calculate_points(k: int, tbl: List[int]) -> int:
#     counts = [0] * 10
#     for row in tbl:
#         for val in row:
#             index = int(val) if val != '.' else 0
#             counts[index] += 1
#     points = 0
#     fingers = 2 * k
#     for i in range(1, len(counts)):
#         if fingers >= counts[i] and counts[i] != 0:
#             points += 1
#     return points
# k, tbl = read_input()
# print(calculate_points(k, tbl))
# endregion

# endregion
# ===============================================================================================