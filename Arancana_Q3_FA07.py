students_data = [
    [13, 6, 2],
    [14, 7, 3],
    [13, 5, 4]
]

print("Student Data (Age, Subjects, Study Hours)")
print("------------------------------------------")

# Print each row clearly
for i in range(len(students_data)):
    print("Student", i + 1, ":", students_data[i])

print("\n--- Summary Per Student ---")

# Calculate total and average per student
for i in range(len(students_data)):
    total = sum(students_data[i])
    average = total / len(students_data[i])
    print("Student", i + 1)
    print("Total:", total)
    print("Average:", average)
    print()

# Find maximum value in entire dataset
max_value = students_data[0][0]

for row in students_data:
    for value in row:
        if value > max_value:
            max_value = value

print("Maximum value in dataset:", max_value)
