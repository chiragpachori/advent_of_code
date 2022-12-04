a = open('input.txt').read()

total = 0
for line in a.splitlines():
    # print(line)
    half_l = int(len(line)/2)
    # print(half_l)
    item = list(set(line[0:half_l]).intersection(set(line[half_l:])))[0]

    if item.isupper():
        total += ord(item) - 38
    else:
        total += ord(item) - 96

print(f"Part 1: {total}")

total = 0
temp = []
for line in a.splitlines():
    temp.append(line)
    if len(temp) == 3:
        d,e,f = temp
        temp = []
        item = list(set(d).intersection(e).intersection(f))[0]
        if item.isupper():
            total += ord(item) - 38
        else:
            total += ord(item) - 96

print(f"Part 2: {total}")