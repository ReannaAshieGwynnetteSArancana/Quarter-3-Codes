names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  # Me
    [4000, 4100, 3900, 4200, 4600],  # Lia
    [6000, 5800, 5900, 6100, 6200]   # Jake
]

print("STEP TRACKER REPORT\n")

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    print(f"{names[i]} - Total: {total} steps | Average: {average:.2f} steps")

print()


highest = steps[0][0]
person_index = 0
day_index = 0

for i in range(len(steps)):
    for j in range(len(steps[i])):
        if steps[i][j] > highest:
            highest = steps[i][j]
            person_index = i
            day_index = j

print("Highest Step Count:")
print(f"{names[person_index]} on {days[day_index]} with {highest} steps\n")

print("Total Steps Per Day:")
for j in range(len(days)):
    day_total = 0
    for i in range(len(steps)):
        day_total += steps[i][j]
    print(f"{days[j]}: {day_total} steps")

print()

overall_total = sum(sum(row) for row in steps)
print(f"Overall Steps (All Friends, All Days): {overall_total
