win_list = ['A Y', 'B Z', 'C X']
draw_dict = ['A X', 'B Y', 'C Z']
lose_list = ['A Z', 'B X', 'C Y']
points_dict = {'X': 1,
               'Y': 2,
               'Z': 3}


with open('input.txt') as f:
    total_points = 0
    for line in f:
        line = line.strip()
        choice_pt = points_dict[line[-1:]]
        round_pt = 0
        if line in win_list:
            round_pt = 6
        elif line in draw_dict:
            round_pt = 3

        final_pt = choice_pt + round_pt
        total_points += final_pt
print(total_points)


def get_score(a_list, letter):
    for entry in a_list:
        if entry[:1] == letter:
            return  points_dict[entry[-1:]]


with open('input.txt') as f:
    total_points = 0
    for line in f:
        line = line.strip()
        round_pt = (points_dict[line[-1:]] - 1) * 3
        choice_pt = 0
        if round_pt == 0:
            choice_pt = get_score(lose_list, line[:1])
        elif round_pt == 3:
            choice_pt = get_score(draw_dict, line[:1])
        elif round_pt == 6:
            choice_pt = get_score(win_list, line[:1])

        final_pt = choice_pt + round_pt
        total_points += final_pt
print(total_points)

