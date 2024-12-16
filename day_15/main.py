class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def left(self):
        return Point(self.x - 1, self.y)
    def right(self):
        return Point(self.x + 1, self.y)
    def up(self):
        return Point(self.x, self.y - 1)
    def down(self):
        return Point(self.x, self.y + 1)


MOVEMENTS = {'<': Point(-1, 0), '>': Point(1, 0), '^': Point(0, -1), 'v': Point(0, 1)}

def get_input_data_raw(filename):
    with open(filename) as f:
        return f.read().split("\n\n")


def get_initial_map(raw_map):
    grid_map = [list(line) for line in raw_map.splitlines()]
    raw_width = len(grid_map[0])+1
    robot_position = raw_map.find("@")
    robot_point = Point(robot_position % raw_width, robot_position // raw_width)
    return robot_point, grid_map


def print_grid(grid_map):

    for row in grid_map:
        print(''.join(row) )


def move_boxes(move, wh_map, moving_boxes):
    new_boxes = []
    first_box = moving_boxes[0]
    box_mark = wh_map[first_box.y][first_box.x]
    for box_pos in moving_boxes:
        new_boxes. append(box_pos + MOVEMENTS[move])
        if box_mark == 'O':
            wh_map[box_pos.y][box_pos.x] = '.'
        if box_mark == '[':
            wh_map[box_pos.y][box_pos.x] = '.'
            wh_map[box_pos.y][box_pos.x + 1] = '.'
    for box_pos in new_boxes:
        if box_mark == 'O':
            wh_map[box_pos.y][box_pos.x] = 'O'
        if box_mark == '[':
            wh_map[box_pos.y][box_pos.x] = '['
            wh_map[box_pos.y][box_pos.x + 1] = ']'


def update_robot_pos(move, robot_pos, wh_map):
    wh_map[robot_pos.y][robot_pos.x] = '.'
    robot_pos = robot_pos + MOVEMENTS[move]
    wh_map[robot_pos.y][robot_pos.x] = '@'
    return robot_pos


def get_gps(wh_map):
    gps = 0
    for j, row in enumerate(wh_map):
        for i, col in enumerate(row):
            if wh_map[j][i] == 'O' or wh_map[j][i] == '[':
                gps += i + 100 * j
    return gps

def expand_map(raw_map):
    new_raw_map = ''
    for position in raw_map:
        if position == '@':
            new_raw_map += '@.'
        elif position == '#':
            new_raw_map += '##'
        elif position == '.':
            new_raw_map += '..'
        elif position == 'O':
            new_raw_map += '[]'
        else:
            new_raw_map += position
    return new_raw_map


def get_moving_boxes(wh_map, move, robot_pos):
    moving_obstacles = []
    pos_to_explore = [robot_pos + MOVEMENTS[move]]
    while pos_to_explore:
        next_cell_pos = pos_to_explore.pop()
        next_cell_value = wh_map[next_cell_pos.y][next_cell_pos.x]
        if next_cell_value == '[':
            box_left_pos = next_cell_pos
            box_right_pos = next_cell_pos.right()
            moving_obstacles.append(box_left_pos)
            if move == '>':
                new_pos_to_explore = [box_right_pos + MOVEMENTS[move]]
            else:
                new_pos_to_explore = [box_left_pos + MOVEMENTS[move], box_right_pos + MOVEMENTS[move]]
            pos_to_explore.extend(new_pos_to_explore)
        elif next_cell_value == ']':
            box_right_pos = next_cell_pos
            box_left_pos = next_cell_pos.left()
            moving_obstacles.append(box_left_pos)
            if move == '<':
                new_pos_to_explore = [box_left_pos + MOVEMENTS[move]]
            else:
                new_pos_to_explore = [box_left_pos + MOVEMENTS[move], box_right_pos + MOVEMENTS[move]]
            pos_to_explore.extend(new_pos_to_explore)
        elif next_cell_value == '#':
            return None
        elif next_cell_value == 'O':
            moving_obstacles.append(next_cell_pos)
            pos_to_explore.append(next_cell_pos + MOVEMENTS[move])
    return moving_obstacles


def main():
    part = 'part2'
    raw_map, raw_movements = get_input_data_raw("input_data")
    if part == 'part2':
        raw_map = expand_map(raw_map)
    robot_pos, wh_map = get_initial_map(raw_map)
    movements = "".join(raw_movements.split("\n"))
    for move in movements:
        moving_obstacles = get_moving_boxes(wh_map, move, robot_pos)
        if moving_obstacles is not None:
            if moving_obstacles:
                move_boxes(move, wh_map, moving_obstacles)
            robot_pos = update_robot_pos(move, robot_pos, wh_map)
    print(get_gps(wh_map))



if __name__ == "__main__":
    main()