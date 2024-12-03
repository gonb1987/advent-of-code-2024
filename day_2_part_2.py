safe_readings = 0

with open("input_data_day_2") as f:
    for reading_line in f:
        reading_tuple = reading_line.strip().split()
        unsafe_values = 0
        for i in range(len(reading_tuple)-1):
            difference = int(reading_tuple[i + 1]) - int(reading_tuple[i])
            if abs(difference) > 3:
                unsafe_values += 1
            if i == 0:
                if difference > 0:
                    slope = "ascending"
                elif difference < 0:
                    slope = "descending"
                else:
                    unsafe_values += 1
            else:
                if slope == "ascending" and difference <= 0:
                    unsafe_values += 1
                elif slope == "descending" and difference >= 0:
                    unsafe_values += 1
        if unsafe_values <= 1:
            safe_readings += 1

print(f'The number of safe readings is {safe_readings}')