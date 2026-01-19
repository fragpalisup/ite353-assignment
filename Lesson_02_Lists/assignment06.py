import random

random_numbers = [random.randint(1, 20) for _ in range(15)]
print(f"Original list: {random_numbers}")

ascending = sorted(random_numbers)
print(f"Ascending order: {ascending}")

descending = sorted(random_numbers, reverse=True)
print(f"Descending order: {descending}")

unique_numbers = list(set(random_numbers))
unique_numbers.sort()
print(f"Without duplicates: {unique_numbers}")
