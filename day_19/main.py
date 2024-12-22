from collections import defaultdict
from heapq import heappush, heappop

def explore_pattern(pattern):
    matches = []
    index = 0
    different_ways = 0
    tested_patterns = defaultdict(int)
    tested_patterns[0] = 1
    while True:
        previous_n = tested_patterns[index]
        for i in range(1,9):
            new_index = index + i
            if new_index > len(pattern):
                continue
            pattern_part = pattern[index:new_index]
            if pattern_part in components:
                if tested_patterns[new_index] == 0:
                    heappush(matches, new_index)
                if new_index == len(pattern):
                    different_ways += previous_n
                    continue
                tested_patterns[new_index] += previous_n
        try:
            index = heappop(matches)
        except IndexError:
            return different_ways


def components_to_dict(components):
    component_dict = defaultdict(list)
    for component in components:
        component_dict[component[:1]].append(component)
    return component_dict


with open('input_data') as f:
    raw_components, raw_patterns = f.read().split("\n\n")
components = raw_components.strip().split(", ")
component_dict = components_to_dict(components)
patterns = raw_patterns.split("\n")
possible_patterns = dict()
for pattern in patterns:
    possible_patterns[pattern] = explore_pattern(pattern)

print(sum(possible_patterns.values()))
