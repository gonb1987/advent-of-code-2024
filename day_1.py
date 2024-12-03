def load_lists(file_name):
    list1, list2 = [], []
    with open(file_name, "r") as f:
        for line in f:
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))
    return list1, list2


def calc_distance_score(list1, list2):
    total_distance = 0
    sorted_list = zip(sorted(list1), sorted(list2))
    for pair in sorted_list:
        total_distance += abs(pair[0] - pair[1])
    return total_distance


def calc_similarity_score(list1: list[int], list2: list[int]):
    similarity_score = 0
    for n in list1:
        similarity_score += list2.count(n) * n
    return similarity_score


one_list, two_list = load_lists("input_data")
print(f'Distance score is {calc_distance_score(one_list, two_list)}')
print(f'Similarity score is {calc_similarity_score(one_list, two_list)}')
