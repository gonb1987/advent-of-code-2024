from collections import defaultdict
from utils import item_and_next

MOVES = ((0, 1), (0, -1), (-1, 0), (1, 0))
with open('input_data') as f:
    data = f.read().splitlines()
start_pos = None
for i, row in enumerate(data):
    if row.find('S') != -1:
        start_pos = (row.find('S'), i)
        break
visited_positions = {start_pos}
row_dict = defaultdict(list)
row_dict_part_2 = defaultdict(dict)
col_dict = defaultdict(list)
pos = start_pos
index = 0
ended = False
cheats = 0
while True:
    row_dict[pos[1]].append((pos[0], index))
    row_dict_part_2[pos[1]][pos[0]] = index
    col_dict[pos[0]].append((pos[1], index))
    if ended:
        break
    for mov in MOVES:
        new_pos = (pos[0] + mov[0], pos[1] + mov[1])
        if data[new_pos[1]][new_pos[0]] == '.' and (new_pos[0], new_pos[1]) not in visited_positions:
            pos = new_pos
            index += 1
            visited_positions.add((pos[0], pos[1]))
            break
        elif data[new_pos[1]][new_pos[0]] == 'E':
            pos = new_pos
            index += 1
            ended = True


def find_cheats(row_or_col_list):
    cheats = 0
    row_or_col_list.sort(key=lambda x: x[0])
    for item, next_item in item_and_next(row_or_col_list):
        if abs(item[0] - next_item[0]) == 2:
            if abs(item[1] - next_item[1]) > 101:
                cheats += 1
    return cheats


for row in row_dict.values():
    cheats += find_cheats(row)
for col in col_dict.values():
    cheats += find_cheats(col)

print(cheats)
cheats = 0
for pos in visited_positions:
    row, col = pos[1], pos[0]
    index = row_dict_part_2[row][col]
    for i in range(-20, 21):
        if 0 < row + i < 140:
            min_col = max(1, col - 20 + abs(i))
            max_col = min(col + 21 - abs(i), 140)
            cheats_to_explore = set(row_dict_part_2[row + i].keys()).intersection(set(range(min_col, max_col)))
            for cheat in cheats_to_explore:
                if (row_dict_part_2[row + i][cheat] - index) >= 100 + abs(i) + abs(col - cheat):
                    cheats += 1

print(cheats)
