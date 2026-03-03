scores = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 89, 94],
    [70, 75, 72],
    [88, 84, 91]
]

# Print each row clearly
for i in range(len(scores)):
    print("Student", i + 1, "scores:", scores[i])

print("\n--- Summary Per Student ---")

# Calculate total and average per student
for i in range(len(scores)):
    total = sum(scores[i])
    average = total / len(scores[i])
    print("Student", i + 1)
    print("Total:", total)
    print("Average:", average)
    print()

# Find maximum value in entire dataset
max_score = scores[0][0]

for row in scores:
    for value in row:
        if value > max_score:
            max_score = value

print("Highest score in the dataset:", max_score)
