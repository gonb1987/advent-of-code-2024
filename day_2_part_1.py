safe_readings = 0

with open("input_data_day_2") as f:
    for reading_line in f:
        reading_tuple = reading_line.strip().split()
        safe_reading = True
        for i in range(len(reading_tuple)-1):
            difference = int(reading_tuple[i + 1]) - int(reading_tuple[i])
            if abs(difference) > 3:
                safe_reading = False
                break
            if i == 0:
                if difference > 0:
                    slope = "ascending"
                elif difference < 0:
                    slope = "descending"
                else:
                    safe_reading = False
                    break
            else:
                if slope == "ascending" and difference <= 0:
                    safe_reading = False
                    break
                elif slope == "descending" and difference >= 0:
                    safe_reading = False
                    break
        if safe_reading:
            safe_readings += 1

print(f'The number of safe readings is {safe_readings}')