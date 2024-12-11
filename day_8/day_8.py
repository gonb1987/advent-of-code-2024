from itertools import combinations
from collections import defaultdict


def get_pair_distance(first_node, second_node):
    i_distance = first_node[0] - second_node[0]
    j_distance = first_node[1] - second_node[1]
    return i_distance, j_distance


def antinode_in_bounds(antinode, dimensions):
    in_bounds = False
    if 0 <= antinode[0] < dimensions[0]:
        if 0 <= antinode[1] < dimensions[1]:
            in_bounds = True
    return in_bounds


def get_pair_antinodes_part_1(antenna_pair, dimensions):
    antinodes = set()
    first_node = antenna_pair[0]
    second_node = antenna_pair[1]
    i_distance, j_distance = get_pair_distance(first_node, second_node)
    first_antinode = (first_node[0] + i_distance, first_node[1] + j_distance)
    if antinode_in_bounds(first_antinode, dimensions):
        antinodes.add(first_antinode)
    second_antinode = (second_node[0] - i_distance, second_node[1] - j_distance)
    if antinode_in_bounds(second_antinode, dimensions):
        antinodes.add(second_antinode)
    return antinodes

def get_pair_antinodes_part_2(antenna_pair, dimensions):
    first_node = antenna_pair[0]
    second_node = antenna_pair[1]
    antinodes = {first_node, second_node}
    i_distance, j_distance = get_pair_distance(first_node, second_node)
    first_antinode = (first_node[0] + i_distance, first_node[1] + j_distance)
    while antinode_in_bounds(first_antinode, dimensions):
        antinodes.add(first_antinode)
        first_antinode = (first_antinode[0] + i_distance, first_antinode[1] + j_distance)
    second_antinode = (second_node[0] - i_distance, second_node[1] - j_distance)
    while antinode_in_bounds(second_antinode, dimensions):
        antinodes.add(second_antinode)
        second_antinode = (second_antinode[0] - i_distance, second_antinode[1] - j_distance)
    return antinodes

def get_antinodes(antenna_dict, dimensions, part):
    total_antinodes = set()
    for node_type in antenna_dict.keys():
        antenna_pairs = combinations(antenna_dict[node_type], 2)
        for antenna_pair in antenna_pairs:
            if part == "part_1":
                total_antinodes = total_antinodes.union(get_pair_antinodes_part_1(antenna_pair, dimensions))
            if part == "part_2":
                total_antinodes = total_antinodes.union(get_pair_antinodes_part_2(antenna_pair, dimensions))
    return len(total_antinodes)

if __name__ == '__main__':

    with open("input_data") as f:
        raw_data = f.read()
        node_types = set(raw_data) - set('.\n')
        raw_data = raw_data.split('\n')
        map_dimensions = len(raw_data[0]), len(raw_data)
        antennas= defaultdict(list)
        for j, line in enumerate(raw_data):
            for i, location in enumerate(line):
                if location in node_types:
                    antennas[location].append((i, j))

    print(get_antinodes(antennas, map_dimensions, part="part_1"))
    print(get_antinodes(antennas, map_dimensions, part="part_2"))
