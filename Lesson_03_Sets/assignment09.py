# Assignment 9
numbers_set = {1, 2, 3, 4, 5}
print("Original set:", numbers_set)
numbers_list = list(numbers_set)
print("Converted to list:", numbers_list)
numbers_list.append(6)
print("After appending 6:", numbers_list)
final_set = set(numbers_list)
print("Final set:", final_set)