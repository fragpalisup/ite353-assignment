# assignment10.py

original_tuple = (1, 2, 3, 4, 5)
temp_list = list(original_tuple)
temp_list.append(6)
final_tuple = tuple(temp_list)

print(f"Original tuple: {original_tuple}")
print(f"After conversion and append: {final_tuple}")