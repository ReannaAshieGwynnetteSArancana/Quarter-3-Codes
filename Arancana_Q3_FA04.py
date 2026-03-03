names = ["Me", "Lia", "Jake"]

steps = [
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
]

totals = []

# Calculate total steps per person
for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)
    print(names[i], "total steps:", total)

# Find highest and lowest total
highest_total = max(totals)
lowest_total = min(totals)

highest_index = totals.index(highest_total)

print("\nPerson with highest total steps:", names[highest_index])
print("Highest total steps:", highest_total)
print("Lowest total steps:", lowest_total)
print("Difference:", highest_total - lowest_total)
