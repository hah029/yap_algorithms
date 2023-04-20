
# ===============================================================================================
# region Примеры из теории

# region Вариант нахождения скользящего среднего для временного ряда
# endregion

# endregion
# ===============================================================================================

# ===============================================================================================
# region Задачи Яндекс-контест

# region L. Два велосипеда (id=86059152)
# import sys


# def binarySearch(array, left, right, value):
#     if right <= left:
#         if array[right] < value:
#             return -1
#         else:
#             return right
#     mid = (left + right) // 2
#     if array[mid] == value:
#         if array[mid - 1] == value:
#             return binarySearch(array, left, mid, value)
#         else:
#             return mid
#     elif array[mid] > value:
#         return binarySearch(array, left, mid, value)
#     else:
#         return binarySearch(array, mid + 1, right, value)


# def solution(array, value):
#     first_day = binarySearch(array, 0, len(array)-1, value)
#     second_day = binarySearch(array, first_day, len(array)-1, value * 2)
#     first_day = first_day if first_day == -1 else first_day + 1
#     second_day = second_day if second_day == -1 else second_day + 1
#     return first_day, second_day


# def read_input():
#     _ = int(input())
#     input_array = list(map(int, sys.stdin.readline().rstrip().split()))
#     value = int(input())
#     return input_array, value


# if __name__ == '__main__':
#     array, value = read_input()
#     print(*solution(array, value))
# endregion

# region A. Генератор скобок (id=86060342)
# def correct_sequence(prefix):
#     tmp_list = []
#     for ch in prefix:
#         if ch == '(':
#             tmp_list.append(ch)
#         elif ch == ')':
#             if len(tmp_list) == 0:
#                 return False
#             tmp_list.pop()
#     if len(tmp_list) == 0:
#         return True
#     else:
#         return False


# def gen_binary(n, prefix):
#     if n == 0:
#         if correct_sequence(prefix):
#             print(prefix)
#     else:

#         gen_binary(n - 1, prefix + '(')
#         gen_binary(n - 1, prefix + ')')


# def solution(value):
#     gen_binary(value - 1, '(')


# def read_input():
#     value = int(input())
#     return value


# if __name__ == '__main__':
#     value = read_input()
#     solution(value * 2)
# endregion

# region B. Комбинации (id=86061875)
# def gen_binary(n, value_dict, result, prefix):
#     if n == 0:
#         result.append(prefix)
#         return
#     else:
#         for index in range(len(value_dict)):
#             for char in value_dict[index]:
#                 gen_binary(n - 1, value_dict[index + 1:], result, prefix + char)
#     return result


# def solution(array):
#     my_dict = {
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
#     value_dict = [my_dict[ch] for ch in array]
#     result = gen_binary(len(value_dict), value_dict, [], '')
#     return result


# def read_input():
#     value = [*input()]
#     return value


# if __name__ == '__main__':
#     value = read_input()
#     print(*solution(value))
# endregion

# region J. Пузырёк (id=?)
# import sys


# def solution(array, direction='asc'):
#     j = 0
#     flag = True
#     while j < len(array):
#         i = 0
#         tmp = None
#         while i < len(array) - j - 1:
#             if array[i] > array[i + 1]:
#                 tmp = array[i + 1]
#                 array[i + 1] = array[i]
#                 array[i] = tmp
#                 flag = True
#             i += 1
#         if flag:
#             print(*array)
#             flag = False
#         j += 1


# def read_input():
#     _ = input()
#     array = list(map(int, sys.stdin.readline().rstrip().split()))
#     try:
#         _ = input()
#     except:
#         _ = None
#     return array


# if __name__ == '__main__':
#     array = read_input()
#     # read_input()
#     # print(array)
#     solution(array)
    # print(*solution(array), sep='')
# endregion

# region G. Гардероб (id=86116105)
# def solution(array):
#     colors = {
#         0: 0,
#         1: 0,
#         2: 0
#     }
#     for element in array:
#         colors[element] += 1
#     return colors


# def read_input():
#     _ = input()
#     array = list(map(int, input().split()))
#     return array


# if __name__ == '__main__':
#     array = read_input()
#     res = solution(array)
#     print(res[0] * '0 ' + res[1] * '1 ' + res[2] * '2 ')
# endregion


# endregion
# ===============================================================================================

# ===============================================================================================
# region Финальные задания (тоже Яндекс-контест)

# region Задача A: Ближайший ноль (id=84157187)

# endregion

# endregion
# ===============================================================================================
