def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [5, 6, 7, 8, 9, 10, 11, 12]

intersection = list_intersection(list1, list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {sorted(intersection)}")
