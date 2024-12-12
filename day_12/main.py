from collections import defaultdict
from itertools import tee, islice, chain


# Assuming always square gardens.

MOVES= (
    ('left', -1, 0),
    ('right', 1, 0),
    ('up', 0, -1),
    ('down', 0, 1),
)

def item_and_next(some_iterable):
    item_list, next_list = tee(some_iterable, 2)
    next_list = chain(islice(next_list, 1, None), [None])
    return zip(item_list, next_list)


def read_garden_map(filename):
    garden_map = []
    with open(filename) as f:
        for line in f:
            garden_map.append(list(line.strip()))
    return garden_map


def in_bounds(dim, i, j, x, y):
    return (y + j >= 0 and x + i >= 0) and \
        (y + j < dim and x + i < dim)


def process_borders_part_1(borders):
    perimeter = 0
    for line in borders.values():
        perimeter += sum(len(x) for x in line.values())
    return perimeter


def process_borders_part_2(borders):
    sides = 0
    for line in borders.values():
        for border_list in line.values():
            sides += 1
            border_list.sort()
            for num, next_num in item_and_next(border_list):
                if next_num:
                    if num + 1 != next_num:
                        sides += 1
    return sides


def write_border(borders, direction, x, y):
    if direction in ('up', 'down'):
        borders[direction][y].append(x)
    if direction in ('left', 'right'):
        borders[direction][x].append(y)
    return borders


def explore_area(garden_map, i, j, part):
    dim = len(garden_map)
    plot = garden_map[j][i]
    plots_to_explore = {(i, j)}
    current_visited = set()
    area = 0
    borders = {
        'left': defaultdict(list),
        'right': defaultdict(list),
        'up': defaultdict(list),
        'down': defaultdict(list),
    }
    while plots_to_explore:
        x, y = plots_to_explore.pop()
        current_visited.add((x, y))
        area += 1
        for direction, add_x, add_y in MOVES:
            if in_bounds(dim, add_x, add_y, x, y):
                new_plot = garden_map[y + add_y][x + add_x]
                if (x + add_x, y + add_y) in current_visited:
                    continue
                if new_plot == plot:
                    plots_to_explore.add((x + add_x, y + add_y))
                else:
                    borders = write_border(borders, direction, x, y)
            else:
                borders = write_border(borders, direction, x, y)
    if part == 'part_1':
        perimeter = process_borders_part_1(borders)
    elif part == 'part_2':
        perimeter = process_borders_part_2(borders)
    return area, perimeter, current_visited

def calculate_total_price(garden_map, part):
    amount = 0
    dim = len(garden_map)
    total_visited = set()
    for j, row in enumerate(garden_map):
        for i, plot in enumerate(row):
            if (i, j) not in total_visited:
                if part == 'part_1':
                    area, perimeter, visited = explore_area(garden_map, i, j, 'part_1')
                if part == 'part_2':
                    area, perimeter, visited = explore_area(garden_map, i, j, 'part_2')
                amount += area * perimeter
                total_visited = total_visited.union(visited)
    return amount


def main():
    filename = "input_data"
    garden_map = read_garden_map(filename)
    print(calculate_total_price(garden_map, "part_1"))
    print(calculate_total_price(garden_map, "part_2"))


if __name__ == '__main__':
    main()
