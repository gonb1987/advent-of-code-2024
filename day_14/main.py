import re
from math import prod

SPACE_SIZE = (101, 103)
TIME = 100
MAX_TIME = 10000

def move_robot(robot,
               space_size: tuple[int, int],
               time_elapsed: int) -> tuple[int, int]:
    initial_pos = (int(robot.group(1)), int(robot.group(2)))
    velocity = (int(robot.group(3)), int(robot.group(4)))
    final_x = (initial_pos[0] + velocity[0] * time_elapsed) % space_size[0]
    final_y = (initial_pos[1] + velocity[1] * time_elapsed) % space_size[1]
    return final_x, final_y


def get_quadrant(position: tuple[int, int], size: tuple[int, int]) -> int:
    if position[0] == size[0] // 2 or position[1] == size[1] // 2:
        return None
    else:
        return (position[0] // ((size[0] // 2)+1)) + 2 * (position[1] // ((size[1] // 2) +1))


def get_robots_input(filename):
    with open(filename) as f:
        raw_data = f.read()
    robots_regex = re.compile('p=(\d+),(\d+) v=(-?\d+),(-?\d+)')
    return robots_regex.finditer(raw_data)

def fold_y_axis(position: tuple[int, int], size: tuple[int, int]):
    if position[0] > size[0] // 2:
        position = (size[0] - position[0], position[1])
    return position

def main():
    # PART 1
    robots = get_robots_input(filename="input_data")
    quadrants = get_quadrant_distribution(robots, TIME)
    print(prod(quadrants))

    # PART 2
    robots =  list(get_robots_input(filename="input_data"))
    min_folded_positions = None
    for frame_n in range(1, MAX_TIME):
        folded_positions = set(fold_y_axis(move_robot(robot, SPACE_SIZE, frame_n), SPACE_SIZE) for robot in robots)
        if min_folded_positions is None or min_folded_positions > len(folded_positions):
            min_folded_positions = len(folded_positions)
            min_frame = frame_n
    print(min_folded_positions, min_frame)



def get_quadrant_distribution(robots, frame):
    quadrants = [0, 0, 0, 0]
    for robot in robots:
        quadrant = get_quadrant(move_robot(robot, SPACE_SIZE, frame), SPACE_SIZE)
        if quadrant is not None:
            quadrants[quadrant] += 1
    return quadrants


if __name__ == "__main__":
    main()
