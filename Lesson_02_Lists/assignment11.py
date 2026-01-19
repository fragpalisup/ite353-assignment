numbers = list(range(1, 11))
print(f"Original list: {numbers}")

del numbers[6]
del numbers[4]
del numbers[2]
print(f"After removing indices 2, 4, 6: {numbers}")

numbers.insert(5, 99)
print(f"After inserting 99 at index 5: {numbers}")
