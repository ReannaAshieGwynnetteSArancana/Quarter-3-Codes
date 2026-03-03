names = ["Me", "Lia", "Jake"]

steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

daily_totals = []

# Loop by column (day)
for col in range(len(steps[0])):
    total = 0
    for row in range(len(steps)):
        total += steps[row][col]
    daily_totals.append(total)
    print(days[col], "total steps:", total)

# Find most active day
highest_total = max(daily_totals)
highest_index = daily_totals.index(highest_total)

print("\nMost active day overall:", days[highest_index])
print("Total steps that day:", highest_total)
