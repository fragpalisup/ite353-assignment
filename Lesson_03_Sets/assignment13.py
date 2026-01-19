# Assignment 13
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set 1 (before):", set1)
print("Set 2:", set2)
set1.symmetric_difference_update(set2)
print("Set 1 (after symmetric difference update):", set1)