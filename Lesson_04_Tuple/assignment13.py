# assignment13.py

nested_tuple = ((1, 2), (3, 4), (5, 6))

print("Iterating over nested tuple:")
for inner_tuple in nested_tuple:
    for element in inner_tuple:
        print(f"Element: {element}")