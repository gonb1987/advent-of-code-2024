from itertools import combinations


with open("input_data_day_8") as f:
    raw_data = f.read()
    antenna_set = set(raw_data)- set('.\n')
    data = raw_data.split('\n')

def get_antenna_type_nodes(data, type):
    nodes = []
    for j, line in enumerate(data):
        for i, letter in enumerate(line):
            if letter == type:
                nodes.append((i,j))

