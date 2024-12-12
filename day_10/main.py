MOVES = (
    (0,1),
    (1,0),
    (0,-1),
    (-1,0)
)

def get_trailheads(data):
    trailheads = []
    for j, row in enumerate(data):
        for i, col in enumerate(row):
            if data[j][i] == 0:
                trailheads.append((i,j))
    return trailheads


def get_possible_moves(col, row, data):
    value = data[row][col]
    possible_moves = []
    finished_trails = set()
    for i,j in MOVES:
        if col+i >= 0 and row+j >= 0:
            try:
                new_value = data[row + j][col + i]
            except IndexError:
                continue
        else:
            continue
        if new_value == value + 1:
            if new_value == 9:
                finished_trails.add((col+i,row+j))
            else:
                possible_moves.append((col+i,row+j))
    return possible_moves, finished_trails


def get_trailhead_score(trailhead, data):
    finishing_points = set()
    possible_moves = [trailhead]
    while len(possible_moves) > 0:
        test_postion = possible_moves.pop()
        new_moves, finished = get_possible_moves(test_postion[0], test_postion[1], data)
        finishing_points = finishing_points.union(finished)
        possible_moves.extend(new_moves)
    return len(finishing_points)

def get_trailhead_score_diff_paths(trailhead, data):
    score = 0
    possible_moves = [trailhead]
    while len(possible_moves) > 0:
        test_postion = possible_moves.pop()
        new_moves, finished = get_possible_moves(test_postion[0], test_postion[1], data)
        score += len(finished)
        possible_moves.extend(new_moves)
    return score


def get_total_score(data, part='part1'):
    total = 0
    trailheads = get_trailheads(data)
    for trailhead in trailheads:
        if part == 'part1':
            trailhead_score = get_trailhead_score(trailhead, data)
        if part == 'part2':
            trailhead_score = get_trailhead_score_diff_paths(trailhead, data)
        total += trailhead_score
    return total


def main():
    data = []
    filename = 'input_file'
    with open(filename) as f:
        for line in f.readlines():
            data.append([int(x) for x in line.strip()])
    total_score_part_1 = get_total_score(data, 'part1')
    total_score_part_2 = get_total_score(data, 'part2')
    print(total_score_part_1)
    print(total_score_part_2)


if __name__ == "__main__":
    main()