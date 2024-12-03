import re

product = 0
with open('input_data_day_3') as f:
    data = f.read()
    valid_regex = re.compile('mul\((\d+),(\d+)\)')
    factor_pairs = valid_regex.findall(data)
    for pair in factor_pairs:
        product += int(pair[0])*int(pair[1])

print(product)