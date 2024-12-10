from itertools import product

OPERATIONS = ['+', 'x']
OPERATIONS_PART_2 = ['+', 'x', '||']

with open("input_data_day_7") as f:
    data = []
    for line in f:
        result, operands = line.strip().split(':')
        operands = [int(x) for x in operands.strip().split(' ')]
        data.append((int(result), operands))
total_value = 0
for register in data:
    for combination in product(OPERATIONS, repeat=len(register[1])-1):
        calculated_result = register[1][0]
        for i, operation in enumerate(combination):
            if operation == '+':
                calculated_result += register[1][i+1]
            if operation == 'x':
                calculated_result *= register[1][i+1]
        if calculated_result == register[0]:
            total_value += register[0]
            break
        elif calculated_result > register[0]:
            break
print(total_value)

total_value = 0
for register in data:
    for combination in product(OPERATIONS_PART_2, repeat=len(register[1])-1):
        calculated_result = register[1][0]
        for i, operation in enumerate(combination):
            if operation == '+':
                calculated_result += register[1][i+1]
            if operation == 'x':
                calculated_result *= register[1][i+1]
            if operation == '||':
                calculated_result = int(str(calculated_result)+str(register[1][i+1]))
        if calculated_result == register[0]:
            total_value += register[0]
            break
print(total_value)