from collections import defaultdict
from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        return (self.x, self.y)

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

    def look(self, direction=None, position=None):
        if position is None:
            position = self.position
        if direction is None:
            direction = self.direction
        if direction == 'east':
            position = Point(self.position.x + 1, self.position.y)
        elif direction == 'south':
            position = Point(self.position.x, self.position.y + 1)
        elif direction == 'north':
            position = Point(self.position.x, self.position.y - 1)
        elif direction == 'west':
            position = Point(self.position.x - 1, self.position.y)
        return position, self.get_cell_value(position)

    def move(self, direction):
        if direction == 'east':
            self.position = Point(self.postion.x + 1, self.position.y)
        if direction == 'south':
            self.position = Point(self.position.x, self.position.y + 1)
        if direction == 'north':
            self.position = Point(self.position.x, self.position.y - 1)
        if direction == 'west':
            self.position = Point(self.position.x - 1, self.position.y)
        self.visited_cells.append(self.position)
        return self.grid_map[self.position.y][self.position.x]


class Maze(Grid):


    def __init__(self, raw_map, starting_direction):
        super().__init__(raw_map)
        self.start, self.end = self.find_start_end_points()
        self.position = self.start
        self.vertices = self.get_vertices()
        self.direction = starting_direction
        self.visited_cells = [self.start]
        self.discovered_vertices = {self.start}
        self.connections = defaultdict(set)


    def get_vertices(self):
        vertices = []
        for j, row in enumerate(self.grid_map):
            for i, col in enumerate(row):
                position = Point(i, j)
                if self.get_cell_value(position) not in '#SE':
                    surrounding_positions = [self.look(direction, position)[1] for direction in self.DIRECTIONS]
                    if surrounding_positions.count('.') > 2:
                        vertices.append(Point(i, j))
        return vertices

    def get_possible_directions(self):
        possible_paths = []
        for direction in self.DIRECTIONS:
            neighbour, value = self.look(direction)
            if value == '.' and neighbour not in self.visited_cells:
                possible_paths.append(direction)
        return possible_paths

    def find_start_end_points(self):
        for j, row in enumerate(self.grid_map):
            if 'E' in row:
                end = Point(row.index('E'), j)
            if 'S' in row:
                start = Point(row.index('S'), j)
        return start, end

    def get_connections(self):
        while self.discovered_vertices:
            vertex = self.discovered_vertices.pop()
            self.position = vertex
            directions = self.get_possible_directions()
            for direction in directions:
                path_direction = direction
                path_cost = 0
                while True:
                    if self.look(path_direction)[1] == '.':
                        self.move(path_direction)
                        path_cost += 1
                        if self.position in self.vertices:
                            self.connections[vertex].append((self.position, path_cost))
                            self.discovered_vertices.append(self.position)
                            break
                    else:
                        path_direction = self.get_possible_directions()
                        if path_direction:

                            path_cost += 1000
                        else:
                            break



