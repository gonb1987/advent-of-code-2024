with open("input_data_day_4") as f:
    char_matrix = []
    for line  in f:
        char_matrix.append(list(line.strip()))

directions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
)
counter = 0
rows = len(char_matrix)
cols = len(char_matrix[0])

for i in range(rows):
    for j in range(cols):
        if char_matrix[i][j] == 'X':
            for hor, ver in directions:
                # Check if the end of the string in this direction is in bounds. If not, continue over to the next direction
                if rows -1 >= i+3*hor >= 0 and cols -1 >= j + 3 * ver >= 0:
                    word = char_matrix[i+hor][j+ver] + \
                        char_matrix[i+2*hor][j+2*ver] + \
                        char_matrix[i+3*hor][j+3*ver]
                    if word == 'MAS':
                        counter += 1
                else:
                    continue
        else:
            continue

print(counter)