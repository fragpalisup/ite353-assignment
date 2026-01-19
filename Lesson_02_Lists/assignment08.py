students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'Diana', 'score': 95},
    {'name': 'Eve', 'score': 88}
]

print("Original list:")
for student in students:
    print(student)

sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)

print("\nSorted by score (descending):")
for student in sorted_students:
    print(student)
