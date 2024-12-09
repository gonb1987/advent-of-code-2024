from typing import TextIO, List, Tuple


f: TextIO
with open("input_data_day_5", "r") as f:
    input_data = f.read().split('\n\n')
order_rules: list[tuple[str, str]]= []
updates: list[list[int]] = []
for line in input_data[0].split():
    after: str
    before: str
    before, after = line.split('|')
    order_rules.append((int(before), int(after)))
for line in input_data[1].split():
    numbers = [int(x) for x in line.split(',')]
    updates.append(numbers)
middle_values: list[int] = []
for update in updates:
    correct_order: bool = True
    for before, after in order_rules:
        if before in update and after in update:
            if update.index(after) < update.index(before):
                correct_order = False
    if correct_order:
        middle_values.append(update[len(update)//2])
print(sum(middle_values))






