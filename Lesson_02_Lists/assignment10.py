def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

print(f"Original nested list: {nested}")
print(f"Flattened list: {flatten_list(nested)}")
