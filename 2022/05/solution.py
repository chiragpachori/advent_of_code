import string
from parse import parse

a = open('input').read()

# Every vertical pile of crates is a list with the lowest one as 1st element of respective list
block_list = [[], [], [], [], [], [], [], [], []]
for line in reversed(a.splitlines()[:8]):
    j = -1
    for i in range(1, len(line), 4):
        j += 1
        if line[i] in set(string.ascii_uppercase):
            block_list[j].append(line[i])

for line in a.splitlines()[10:]:
    crane_work = parse("move {v1} from {v2} to {v3}", line)
    moves = int(crane_work['v1'])
    move_from = int(crane_work['v2']) - 1
    move_to = int(crane_work['v3']) - 1

    on_crane = block_list[move_from][-moves:]
    block_list[move_from] = block_list[move_from][:-moves]
    block_list[move_to].extend(on_crane)

end_str = ''
for vertical_pile in block_list:
    end_str += str(vertical_pile[-1:][0])
print(end_str)
