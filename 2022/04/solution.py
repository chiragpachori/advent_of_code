a = open('input').read()

total_part_1 = 0
total_part_2 = 0

for line in a.splitlines():
    # x, y are two sets created by splitting the line at ',' and taking the '-' separated numbers for range
    x = set(range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])+1))
    y = set(range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])+1))

    if x.issubset(y) or y.issubset(x):
        total_part_1 += 1

    if len(x.intersection(y)) > 0:
        total_part_2 += 1

print(f"Part 2: {total_part_1}")
print(f"Part 2: {total_part_2}")

# Single line solutions:
print(sum([int(set(range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])+1)).issubset(set(range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])+1))) or set(range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])+1)).issubset(set(range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])+1)))) for line in a.splitlines()]))
print(sum([int(len(set(range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])+1)).intersection(set(range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])+1))))) > 0 for line in a.splitlines()]))

