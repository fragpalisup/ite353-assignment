def rotate_list(lst, n):
    if not lst:
        return lst
    n = n % len(lst)
    return lst[-n:] + lst[:-n] if n != 0 else lst

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotated_3 = rotate_list(original, 3)
rotated_5 = rotate_list(original, 5)

print(f"Original list: {original}")
print(f"Rotated by 3 positions: {rotated_3}")
print(f"Rotated by 5 positions: {rotated_5}")
