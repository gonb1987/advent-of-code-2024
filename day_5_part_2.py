from typing import TextIO, List, Tuple

def swap_values(ind_a: int, ind_b: int, swap_list: list) -> None :
    swap_list[ind_a], swap_list[ind_b] = swap_list[ind_b], swap_list[ind_a]


def check_update(update, rules) -> bool:
    correct = True
    for before, after in rules:
        if update.index(before) > update.index(after):
            correct = False
    return correct


def sort_update(update, rules) -> None:
    while not check_update(update, rules):
        for before, after in rules:
            if update.index(before) > update.index(after):
                swap_values(update.index(after), update.index(before), update)


def get_applicable_rules(update, rules):
    applicable_rules = []
    for before, after in rules:
        if before in update and after in update:
            applicable_rules.append((before, after))
    return applicable_rules


f: TextIO
with open("input_data_day_5", "r") as f:
    input_data = f.read().split('\n\n')
order_rules: list[tuple[str, str]]= []
updates: list[list[int]] = []
for line in input_data[0].split():
    after_str: str
    before_str: str
    before_str, after_str = line.split('|')
    order_rules.append((int(before_str), int(after_str)))
for line in input_data[1].split():
    numbers = [int(x) for x in line.split(',')]
    updates.append(numbers)
middle_values: list[int] = []
for update in updates:
    rules = get_applicable_rules(update, order_rules)
    if not check_update(update, rules):
        sort_update(update, rules)
        middle_values.append(update[len(update)//2])
print(sum(middle_values))






