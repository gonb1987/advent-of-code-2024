from collections import defaultdict
from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.y < other.y:
                return True
        return False

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def left(self):
        return Point(self.x - 1, self.y)

    def right(self):
        return Point(self.x + 1, self.y)

    def up(self):
        return Point(self.x, self.y - 1)

    def down(self):
        return Point(self.x, self.y + 1)

    def get_surrounding(self, grid):
        return {
            self.up(): grid.get_cell_value(self.up()),
            self.down(): grid.get_cell_value(self.down()),
            self.left(): grid.get_cell_value(self.left()),
            self.right(): grid.get_cell_value(self.right())
        }
    def get_tuple(self):
        return self.x, self.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Grid:
    DIRECTIONS = {'north', 'west', 'south', 'east'}
    def __init__(self, raw_map):
        self.grid_map = [list(line) for line in raw_map.splitlines()]
        self.position = None
        self.visited_cells = []

    def get_cell_value(self, point: Point):
        return self.grid_map[point.y][point.x]

    def look(self, direction, position=None):
        if position is None:
            position = self.position
        if direction is None:
            direction = self.direction
        if direction == 'east':
            position = Point(position.x + 1, position.y)
        elif direction == 'south':
            position = Point(position.x, position.y + 1)
        elif direction == 'north':
            position = Point(position.x, position.y - 1)
        elif direction == 'west':
            position = Point(position.x - 1, position.y)
        return position, self.get_cell_value(position)

    def move(self, direction):
        if direction == 'east':
            self.position = Point(self.position.x + 1, self.position.y)
        if direction == 'south':
            self.position = Point(self.position.x, self.position.y + 1)
        if direction == 'north':
            self.position = Point(self.position.x, self.position.y - 1)
        if direction == 'west':
            self.position = Point(self.position.x - 1, self.position.y)
        self.visited_cells.append(self.position)
        return self.grid_map[self.position.y][self.position.x]





