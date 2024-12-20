from heapq import heappush, heappop, heapify

with open('input_data') as f:
    raw_components, raw_patterns = f.read().split("\n\n")
components = raw_components.strip().split(", ")
patterns = raw_patterns.split("\n")

for pattern in patterns:
    matches = []
    composed_word = ''
    index = 0
    for component in components:
        if component == pattern[index:index + len(component)]:
            matches.append((composed_word + component, index + len(component)))
            new_index = index + len(component)