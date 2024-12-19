# Get vertex list (coordinates). A vertex is a point surrounded by 3 or 4 point in the cardinal directions.
# Start and End points are also vertex.
# Get vertex connections and cost
from collections import defaultdict
from heapq import heappush, heappop, heapify
from utils import Point, Grid

OPPOSITE = {
    'north': 'south',
    'south': 'north',
    'east': 'west',
    'west': 'east',
}

class Maze(Grid):


    def __init__(self, raw_map, starting_direction):
        super().__init__(raw_map)
        self.start, self.end = self.find_start_end_points()
        self.position = self.start
        self.vertices = self.get_vertices()
        self.direction = starting_direction
        self.visited_cells = [self.start]
        self.discovered_vertices = {self.start}
        self.connections = defaultdict(list)


    def get_vertices(self):
        vertices = [self.start, self.end]
        for j, row in enumerate(self.grid_map):
            for i, col in enumerate(row):
                position = Point(i, j)
                if self.get_cell_value(position) not in '#SE':
                    surrounding_positions = [self.look(direction, position)[1] for direction in self.DIRECTIONS]
                    if surrounding_positions.count('.') > 2:
                        vertices.append(Point(i, j))
        return vertices

    def get_possible_directions(self, point=None, check_visited=True):
        if point is None:
            point = self.position
        possible_paths = []
        for direction in self.DIRECTIONS:
            neighbour, value = self.look(direction, point)
            if value in '.ES':
                if check_visited:
                    if neighbour not in self.visited_cells:
                        possible_paths.append(direction)
                else:
                    possible_paths.append(direction)
        return possible_paths

    def find_start_end_points(self):
        start = None
        end = None
        for j, row in enumerate(self.grid_map):
            if 'E' in row:
                end = Point(row.index('E'), j)
            if 'S' in row:
                start = Point(row.index('S'), j)
        return start, end

    def dijkstra(self, start, start_dir, end):
        self.visited_cells = {start}
        reachable = self.get_reachable(start, start_dir)
        shortest_distances = {start: (0, (start, ))}
        heapify(reachable)
        while reachable:
            step_cost, next_step, current_step, direction = heappop(reachable)
            if next_step in self.visited_cells:
                continue
            shortest_distances[next_step] = (
                step_cost,
                shortest_distances[current_step][1] + (next_step, )
            )
            self.visited_cells.add(next_step)
            next_points = self.get_reachable(next_step, direction)
            for next_point in next_points:
                next_point_cost = shortest_distances[next_step][0] + next_point[0]
                heappush(reachable, (next_point_cost, next_point[1], next_point[2], next_point[3]))
        return shortest_distances





    def get_reachable(self, point, current_direction):
        reachable = []
        directions = self.get_possible_directions(point, check_visited=True)
        for direction in directions:
            if direction == current_direction:
                cost = 1
            else:
                cost = 1001
            next_point, _ = self.look(direction, point)
            reachable.append((cost, next_point, point, direction))
        return reachable





    def get_connections(self):
        for vertex in self.vertices:
            directions = self.get_possible_directions(point=vertex, check_visited=False)
            for direction in directions:
                self.position = vertex
                self.visited_cells = [vertex]
                starting_direction = path_direction = direction
                path_cost = 0
                while True:
                    if self.look(path_direction)[1] == '.':
                        self.move(path_direction)
                        path_cost += 1
                        if self.position in self.vertices:
                            self.connections[vertex].append((self.position, path_cost, starting_direction, path_direction))
                            self.discovered_vertices.add(self.position)
                            break
                    else:
                        path_direction = self.get_possible_directions()
                        if path_direction:
                            path_direction = path_direction[0]
                            path_cost += 1000
                        else:
                            break

def main():
    with open("input_data") as f:
        raw_map  =  f.read()
    maze = Maze(raw_map, 'east')
    solution = maze.dijkstra(maze.start, maze.direction, maze.end)
    vertices = set(maze.get_vertices())
    shortest_path = set(solution[maze.end][1])
    vertices_in_sp = vertices.intersection(shortest_path)
    while vertices_in_sp:
        vertex = vertices_in_sp.pop()
        vertex_cost = solution[vertex][0]
        directions = maze.get_possible_directions(point=vertex, check_visited=False)
        for direction in directions:
            point = maze.look(direction, vertex)[0]
            opposite_point = maze.look(OPPOSITE[direction], vertex)[0]
            if point not in shortest_path and opposite_point in shortest_path:
                if solution[point][0] == vertex_cost + 999:
                    new_path = set(solution[point][1])
                    alternative_path = new_path.difference(shortest_path)
                    new_vertices = alternative_path.intersection(vertices)
                    vertices_in_sp = vertices_in_sp.union(new_vertices)
                    shortest_path = shortest_path.union(new_path)
    print(len(shortest_path))






if __name__ == "__main__":
    main()









