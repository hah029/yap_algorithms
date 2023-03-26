
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



# endregion
# ===============================================================================================

# ===============================================================================================
# region Финальные задания (тоже Яндекс-контест)

# region Задача A: Ближайший ноль (id=84157187)

# endregion

# endregion
# ===============================================================================================
