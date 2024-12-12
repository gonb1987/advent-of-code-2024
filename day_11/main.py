from functools import cache


@cache
def transform_stone(stone):
        if stone == '0':
            return ('1',)
        elif len(stone) % 2 == 0:
            return (stone[:len(stone)//2],
                    str(int(stone[len(stone)//2:])))
        else:
            new_value = int(stone) * 2024
            return (str(new_value),)

@cache
def calculate_num_stones(stone, blinks):
    if blinks == 0:
        return 1
    transformed = transform_stone(stone)
    stone_num = 0
    for stone in transformed:
        stone_num += calculate_num_stones(stone, blinks - 1)
    return stone_num


def main():
    filename = 'input_data'
    with open(filename) as f:
        stones = f.read().strip().split()
    num_stones = 0
    blinks = 75
    for stone in stones:
        new_stones = calculate_num_stones(stone, blinks)
        num_stones += new_stones
    print(num_stones)


if __name__ == '__main__':
    main()