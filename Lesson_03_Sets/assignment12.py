# Assignment 12
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)
while my_set:
    removed = my_set.pop()
    print(f"Removed: {removed}, Remaining set: {my_set}")
print("\nFinal set (empty):", my_set)