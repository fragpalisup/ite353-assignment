# Assignment 14
my_set = {10, 20, 30, 40, 50}
print("Set:", my_set)
test_elements = [10, 25, 30, 60, 50]
for element in test_elements:
    if element in my_set:
        print(f"{element} is in the set")
    else:
        print(f"{element} is NOT in the set")