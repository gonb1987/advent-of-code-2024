with open("input_data_day_4") as f:
    char_matrix = []
    for line  in f:
        char_matrix.append(list(line.strip()))

counter = 0
rows = len(char_matrix)
cols = len(char_matrix[0])
# Discard the first and last rows and columns, as no matches are possible there and to avoid IndexErrors
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if char_matrix[i][j] == 'A':
            # Concatenate all the diagonal values in a consistent order and see if they match one of the valid sequences
            word = char_matrix[i-1][j-1] + \
                char_matrix[i-1][j+1] + \
                char_matrix[i+1][j-1] + \
                char_matrix[i+1][j+1]
            if word in ('MMSS', 'MSMS', 'SMSM', 'SSMM'):
                counter += 1
        else:
            continue

print(counter)