from itertools import combinations_with_replacement
import re

# ASSUMPTION: ALL BUTTONS ADD A POSITIVE VALUE

BUTTON_A_COST = 3
BUTTON_B_COST = 1

def process_input_data(filename, part='part_1'):
    button_a_re = re.compile('Button A: X\+(\d+), Y\+(\d+)')
    button_b_re = re.compile('Button B: X\+(\d+), Y\+(\d+)')
    prize_re = re.compile('Prize: X\=(\d+), Y\=(\d+)')
    with open(filename) as f:
        raw_data = f.read()
    a_buttons = map(lambda x: (int(x[0]),int(x[1])), button_a_re.findall(raw_data))
    b_buttons = map(lambda x: (int(x[0]),int(x[1])), button_b_re.findall(raw_data))
    if part == 'part_1':
        delta = 0
    elif part == 'part_2':
        delta = 10000000000000
    prizes = map(lambda x: (int(x[0]) + delta, int(x[1]) + delta), prize_re.findall(raw_data))
    return zip(a_buttons, b_buttons, prizes)
def main():
    filename = "input_data"
    part = 'part_1'
    data = process_input_data(filename, part)
    total_cost = 0
    for (a,d), (b,e), (c,f) in data:
        if (f*a-d*c) % (e*a-d*b) == 0:
            b_presses = (f*a-d*c) // (e*a-d*b)
            if (c - (b_presses * b)) % a == 0:
                a_presses = (c - (b_presses * b)) // a
                total_cost += b_presses * BUTTON_B_COST + a_presses * BUTTON_A_COST
    print(total_cost)


if __name__ == "__main__":
    main()