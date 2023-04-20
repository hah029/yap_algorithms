
# ===============================================================================================
# region Примеры из теории

# region Вариант нахождения скользящего среднего для временного ряда
# endregion

# endregion
# ===============================================================================================

# ===============================================================================================
# region Задачи Яндекс-контест

# region B. Список дел
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
# def solution(node):
#     while node:
#         print(node.value)
#         node = node.next_item
# def read_input():
#     count = int(input())
#     input_array = [input() for _ in range(count)]
#     return input_array
# if __name__ == '__main__':
#     arr = read_input()
#     node_next = None
#     for val in arr:
#         node_prev = Node(val, node_next)
#         node_next = node_prev
#     solution(node_prev)
# endregion

# region C. Нелюбимое дело
# LOCAL = True

# if LOCAL:
# 	class Node:
# 		def __init__(self, value, next_item=None):
# 			self.value = value
# 			self.next_item = next_item

# def solution(node, idx):
# 	if idx == 0:
# 		return node.next_item
# 	prev_node = None
# 	current_node = node
# 	next_node = node.next_item
# 	for i in range(1, idx + 1):
# 		prev_node = current_node
# 		current_node = next_node
# 		next_node = current_node.next_item

# 	prev_node.next_item = next_node
# 	return node

# def print_list(node):
#     while node:
#         print(node.value)
#         node = node.next_item

# def read_input():
# 	count = int(input())
# 	input_array = [input() for _ in range(count)]
# 	index_to_delete = int(input())
# 	return input_array, index_to_delete

# if __name__ == '__main__':
# 	arr, index_to_delete = read_input()
# 	node_next = None
# 	for val in arr:
# 		node_prev = Node(val, node_next)
# 		node_next = node_prev
# 	print_list(solution(node_prev, index_to_delete))
# endregion

# region D. Заботливая мама
# LOCAL = True


# if LOCAL:
# 	class Node:
# 		def __init__(self, value, next_item=None):
# 			self.value = value
# 			self.next_item = next_item


# def read_input():
# 	count = int(input())
# 	input_array = [input() for _ in range(count)]
# 	element = input()
# 	return input_array, element


# def solution(node, elem):
# 	index = 0
# 	current = node
# 	while current is not None:
# 		if current.value == elem:
# 			return index
# 		current = current.next_item
# 		index += 1
# 	return -1


# def test():
# 	arr, element = read_input()
# 	node_next = None
# 	for val in arr:
# 		node_prev = Node(val, node_next)
# 		node_next = node_prev
# 	print(solution(node_prev, element))


# if __name__ == '__main__':
# 	test()
# endregion

# region E. Всё наоборот
# LOCAL = True
# if LOCAL:
#     class DoubleConnectedNode:  
#         def __init__(self, value, next=None, prev=None):
#             self.value = value
#             self.next = next
#             self.prev = prev

# def solution(node):
#     temp = None
#     current = node
#     while current:
#         temp = current.prev
#         current.prev = current.next
#         current.next = temp
#         current = current.prev

#     if temp:
#         node = temp.prev
#     return node

# def read_input():
# 	count = int(input())
# 	input_array = [input() for _ in range(count)]
# 	return input_array


# def print_list(node):
# 	while node:
# 		print(node.value)
# 		node = node.next

# def two_direction_list_generate(arr):
# 	temp_node_list = []

# 	for value in arr:
# 		node = DoubleConnectedNode(value, None, None)
# 		temp_node_list.append(node)

# 	for index, current in enumerate(temp_node_list):
# 		if index == 0:
# 			current.prev = None
# 		else:
# 			current.prev = temp_node_list[index - 1]

# 		if index == (len(temp_node_list) - 1):
# 			current.next = None
# 		else:
# 			current.next = temp_node_list[index + 1]

# 	return temp_node_list[0]

# def test():
# 	input_array = read_input()
# 	node = two_direction_list_generate(input_array)
# 	new_head = solution(node)
# 	print_list(new_head)

# if __name__ == '__main__':
#     test()
# endregion

# region F. Стек - Max
# class StackMax:
#     def __init__(self):
#         self.items = []

#     def push(self, value):
#         self.items.append(value)

#     def pop(self):
#         if len(self.items) == 0:
#             print('error')
#             return
#         return self.items.pop()

#     def get_max(self):
#         if len(self.items) == 0:
#             return None
#         return max(self.items)


# def read_input():
#     count = int(input())
#     input_array = [input().split() for _ in range(count)]
#     return input_array


# def test():
#     input_array = read_input()
#     stack = StackMax()

#     for item in input_array:
#         if item[0] == 'push':
#             stack.push(int(item[1]))
#         elif item[0] == 'pop':
#             stack.pop()
#         elif item[0] == 'get_max':
#             print(stack.get_max())


# if __name__ == '__main__':
#     test()
# endregion

# region F. Стек - Max
# class StackMaxEffective:
#     def __init__(self):
#         self.items = []
#         self.max_value = {
#             'prev': None,
#             'cur': None
#         }

#     def push(self, value):
#         self.items.append(value)
#         if self.max_value['cur'] is None:
#             self.max_value['cur'] = value
#         elif value > self.max_value['cur']:
#             self.max_value['prev'] = self.max_value['cur']
#             self.max_value['cur'] = value

#     def pop(self):
#         if len(self.items) == 0:
#             print('error')
#             return
#         item = self.items.pop()
#         if len(self.items) == 0:
#             self.max_value['prev'] = None
#             self.max_value['cur'] = None
#         elif item == self.max_value['cur']:
#             self.max_value[;] = max(self.items)
#         return item

#     def get_max(self):
#         return self.max_value['cur']


# def read_input():
#     count = int(input())
#     input_array = [input().split() for _ in range(count)]
#     return input_array


# def test():
#     input_array = read_input()
#     stack = StackMaxEffective()

#     for item in input_array:
#         if item[0] == 'push':
#             stack.push(int(item[1]))
#         elif item[0] == 'pop':
#             stack.pop()
#         elif item[0] == 'get_max':
#             print(stack.get_max())


# if __name__ == '__main__':
#     test()
# endregion

# region

# cache = {0: 1, 1: 1}


# def solution_recursive(num):
#     if num in cache:
#         return cache[num]
#     cache[num] = solution_recursive(num - 1) + solution_recursive(num - 2)
#     return cache[num]


# def solution_iterative(num, k):
#     if num in [0, 1]:
#         return 1

#     res = []

#     previous, fib_number = 0, 1
#     for _ in range(1, num + 1):
#         previous, fib_number = fib_number, previous + fib_number
#         res.append(fib_number % pow(10, k))

#     return res


def read_input():
    arr = list(map(int, [*input().split()]))
    n = arr[0]
    k = arr[1]
    return n, k

def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


# Calculate Fn mod m
def fibonacciModulo(n, m):
    # Getting the period
    pisano_period = pisanoPeriod(m)

    # Taking mod of N with
    # period length
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        previous, current = current, previous + current

    return (current % m)


# Driver Code
if __name__ == '__main__':
    print([pisanoPeriod(val) for val in [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]])
    periods = [60, 300, 1500, 15000, 150000, 1500000, 15000000, 150000000]
    # n, m = read_input()
    # print(fibonacciModulo(n, 10 ** m))


# def test():
#     n, k = read_input()
#     periods = []
#     result = {
#         1: 60,
#         2: 300,
#         3: 1500,
#         4: 15000,
#         5: 15000,
#         6: 15000,
#         7: 15000,
#         8: 15000,
#     }
#     # for i in range(n):
#     #     result.append(solution_iterative(i, k) % pow(10, k))
#     print(result)


# if __name__ == '__main__':
#     test()
# endregion


# endregion
# ===============================================================================================

# ===============================================================================================
# region Финальные задания (тоже Яндекс-контест)

# region Задача A: Ближайший ноль (id=84157187)

# endregion

# endregion
# ===============================================================================================
