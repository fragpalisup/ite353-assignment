# Assignment 10
dict_with_set_keys = {
    frozenset([1, 2]): 10,
    frozenset([3, 4]): 20,
    frozenset([5, 6]): 30
}
print("Dictionary with frozenset keys:")
for key, value in dict_with_set_keys.items():
    print(f"  {key}: {value}")