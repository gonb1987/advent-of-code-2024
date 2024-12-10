from copy import deepcopy

directions = ('^', '>', 'v', '<')


class GuardMap:
    def __init__(self, raw_map):
        self.raw_map = raw_map
        self.guard_map = []
        for line in self.raw_map:
            list_pos = []
            for position in line.strip():
                list_pos.append(position)
            self.guard_map.append(list_pos)
        self.map_dimensions = len(self.guard_map[0]), len(self.guard_map)
        self.row: int = 0
        self.col: int = 0
        self.num_loops = 0
        self.traversed = False
        self.visited = set()
        self.direction = ''
        self.starting_pos = self.get_starting_position()

    def get_starting_position(self):
        for row_num, row in enumerate(self.guard_map):
            for col_num, cell_value in enumerate(row):
                if cell_value in directions:
                    self.row = row_num
                    self.col = col_num
                    self.direction = cell_value
                    return row_num, col_num

    def move(self, direction=None, col=None, row=None):
        if direction is None:
            direction = self.direction
        if col is None:
            col = self.col
        if row is None:
            row = self.row
        if direction == '>':
            new_col, new_row = (col + 1, row)
        elif direction == '<':
            new_col, new_row = (col - 1, row)
        elif direction == '^':
            new_col, new_row = (col, row - 1)
        elif direction == 'v':
            new_col, new_row = (col, row + 1)
        return new_col, new_row

    def traverse(self, guard_map=None):
        if guard_map is None:
            guard_map = self.guard_map
        while True:
            new_col, new_row = self.move()
            if self.in_bounds(new_row, new_col):
                if self.check_obstacle(new_row, new_col):
                    # rotate
                    self.mark_position(self.direction)
                    direction_idx = (directions.index(self.direction) + 1) % 4
                    self.direction = directions[direction_idx]
                else:
                    # mark position, add to visited and move cursor

                    self.visited.add((new_row, new_col))
                    self.mark_position(self.direction)
                    self.col, self.row = new_col, new_row
                    if self.check_loop():
                        return True
            else:
                self.mark_position(self.direction)
                self.traversed = True
                return False

    def in_bounds(self, row, col):
        if col < 0 or col >= self.map_dimensions[0] \
                or row < 0 or row >= self.map_dimensions[1]:
            return False
        else:
            return True

    def mark_position(self, symbol, guard_map=None, row=None, col=None):
        if guard_map is None:
            guard_map = self.guard_map
        if row is None:
            row = self.row
        if col is None:
            col = self.col
        self.guard_map[row][col] += symbol

    def check_obstacle(self, row, col) -> str:
        cell = self.guard_map[row][col]
        if  cell == '#':
            return True
        else:
            return False

    def check_loop(self):
        if self.direction in self.guard_map[self.row][self.col]:
            return True
        else:
            return False

    def count_loops(self):
        if not self.traversed:
            self.traverse()
        pos_to_check = self.visited - set(self.starting_pos)
        for pos in pos_to_check:
            # Add obstacle in position
            new_raw_map = deepcopy(self.raw_map)
            new_raw_map[pos[0]] = (
                    new_raw_map[pos[0]][:pos[1]] +
                    '#' +
                    new_raw_map[pos[0]][pos[1] + 1:]
            )
            new_guard_map = GuardMap(new_raw_map)
            if new_guard_map.traverse():
                self.num_loops += 1

with open('input_data_day_6') as f:
    raw_map = f.readlines()

map = GuardMap(raw_map)
map.traverse()
map.count_loops()
print(f'Number of positions where a loop can be created: {map.num_loops}')