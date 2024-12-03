import re

product = 0
with open('input_data_day_3') as f:
    data = f.read()
    # Remove the pieces of data in between a don't and the following do
    dont_re = re.compile("don't\(\)")
    do_re = re.compile("do\(\)")
    start_pos = 0
    while True:
        dont_match = dont_re.search(data, start_pos)
        if dont_match:
            do_match = do_re.search(data, dont_match.span()[1])
            if do_match:
                data = data[:dont_match.span()[0]] + data[do_match.span()[1]:]
            else:
                data = data[:dont_match.span()[0]]
                break
        else:
            break
    # Solve for the sanitized data
    valid_regex = re.compile('mul\((\d+),(\d+)\)')
    factor_pairs = valid_regex.findall(data)
    for pair in factor_pairs:
        product += int(pair[0])*int(pair[1])

print(product)