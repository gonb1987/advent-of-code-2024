from heapq import heappush, heappop, heapify

from utils import Point

GRID_SIZE = 71


def get_valid_points(point: Point, invalid_points: list[Point], grid_size: int) -> list[Point]:
    valid_points = []
    points_to_test = point.get_surrounding()
    for point_to_test in points_to_test:
        if point_to_test in invalid_points:
            continue
        if grid_size <= point_to_test.x or point_to_test.x < 0 or \
                grid_size <= point_to_test.y or point_to_test.y < 0:
            continue
        valid_points.append(point_to_test)
    return valid_points


def check_crossed(point, start):
    if abs(start.y - point.y) == GRID_SIZE - 1 or \
            abs(start.x - point.x) == GRID_SIZE - 1 or \
            (start.x == 0 and point.y == 0) or \
            start.y == 0  and point.x == 0 or \
            start.x == GRID_SIZE - 1 and point.y == GRID_SIZE - 1:
        return True
    else:
        return False


def explore_blocked(corrupted_memory: list[Point]) -> [list[Point], int]:
    cross_paths = []
    start_points = [point for point in corrupted_memory if point.x == 0 or point.y == 0 or point.x == GRID_SIZE - 1]
    for start_point in start_points:
        visited = {start_point}
        candidates = [(corrupted_memory.index(start_point), [start_point])]
        heapify(candidates)
        while candidates:
            max_index, path = heappop(candidates)
            last_point = path[-1]
            surrounding_points = last_point.get_surrounding(diagonal=True)
            if check_crossed(last_point, path[0]):
                cross_paths.append((max_index, path))
                break
            surrounding_points = set(surrounding_points).intersection(corrupted_memory)
            not_visited_surrounding_points = surrounding_points.difference(visited)
            for point in not_visited_surrounding_points:
                if point in path:
                    continue
                visited.add(point)
                point_index = corrupted_memory.index(point)
                new_max_index = max(max_index, point_index)
                heappush(candidates, (new_max_index, path + [point]))
    return cross_paths

def explore_memory(corrupted_memory: list[Point]) -> tuple[list[Point], int]:
    current_point = Point(0, 0)
    visited_points = [current_point]
    initial_path = []
    finishing_point = Point(GRID_SIZE - 1, GRID_SIZE - 1)
    paths_to_explore = [
        (len(initial_path), current_point.get_pixel_distance(finishing_point), current_point, initial_path)]
    while paths_to_explore:
        path_length, _, current_point, path = heappop(paths_to_explore)
        next_points = get_valid_points(current_point, corrupted_memory + visited_points, GRID_SIZE)
        for next_point in next_points:
            visited_points.append(next_point)
            new_path = path + [next_point]
            if next_point == finishing_point:
                return new_path, len(new_path)
            heappush(
                paths_to_explore, (
                    len(new_path),
                    next_point.get_pixel_distance(finishing_point),
                    next_point,
                    new_path)
            )


with open('input_data') as f:
    corrupted_memory = list(map(lambda x: Point(int(x.split(',')[0]), int(x.strip().split(',')[1])), f.readlines()))

# PART 1
# shortest_path, shortest_path_length = explore_memory(corrupted_memory[:1024])
# print(shortest_path_length)
# print(shortest_path[-1])

# PART 2
# To prevent the exit from being reachable, there must be a continuous line from left to right or from top to bottom
# attempt to solve it with dijkstra's. We make a heap fo the list of tuples with the points in the border's index
# and object. From there, we pop the lowest index and push the adjacent (including diagonal) points and their index and
# push them into the heap. We must check the first occurrence of a point in a valid opposite border and return the
# biggest index in the path. We must avoid, for each tentative path, going to a point already visited in that path.

cross_paths= explore_blocked(corrupted_memory)
cross_paths.sort()
print(corrupted_memory[cross_paths[0][0]])
