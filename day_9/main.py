def checksum(filesystem):
    checksum = 0
    for i, block in enumerate(filesystem):
        try:
            checksum += int(block) * i
        except ValueError:
            continue
    return checksum


def expand(disk_map):
    filesystem = []
    file_id = 0
    for i, char in enumerate(disk_map):
        if i % 2 == 0:
            for block in range(int(char)):
                filesystem.append(str(file_id))
            file_id  += 1
        else:
            for block in range(int(char)):
                filesystem.append('.')
    return filesystem


def compact(filesystem):
    end_pointer = len(filesystem) - 1
    for i, block in enumerate(filesystem):
        if block == '.':
            while filesystem[end_pointer] == '.':
                end_pointer -= 1
            if i >= end_pointer:
                break
            filesystem[i], filesystem[end_pointer] = filesystem[end_pointer], filesystem[i]
    return filesystem


def defrag(filesystem):
    files = get_files(filesystem)
    spaces = get_spaces(filesystem)
    for file_ind, file_len in files:
        for i, (space_ind, space_len) in enumerate(spaces):
            if space_ind > file_ind:
                break
            if file_len <= space_len:
                for ind in range(file_len):
                    filesystem[space_ind + ind], filesystem[file_ind + ind] = filesystem[file_ind + ind], filesystem[space_ind + ind]
                if file_len == space_len:
                    spaces.remove((space_ind, space_len))
                else:
                    spaces[i] = (space_ind + file_len, space_len - file_len )
                break
    return filesystem


def get_spaces(filesystem: list[str]):
    len_fs = len(filesystem)
    space_list = []
    filesystem_iter = enumerate(filesystem)
    for i, block in filesystem_iter:
        if block == '.':
            start_position = i
            space_len = 1
            while True:
                try:
                    i, block = next(filesystem_iter)
                except StopIteration:
                    space_list.append((start_position, space_len))
                    return space_list
                if block == '.':
                    space_len += 1
                else:
                    break

            space_list.append((start_position, space_len))
    return space_list


def get_files(filesystem: list[str]) :
    file_list = []
    file_id = None
    file_end = None
    file_length = 0
    reverse_filesystem = filesystem[::-1]
    fs_iterator = enumerate(reverse_filesystem)
    for i, block in fs_iterator:
        if block == file_id:
            file_length += 1
        else:
            if file_id is not None:
                file_start = file_end - file_length
                file_list.append((file_start, file_length))
                file_id = None
            if block != '.':
                file_end = len(filesystem) - i
                file_id = block
                file_length = 1
    return file_list


def main():
    with open('input_data', 'r') as f:
        disk_map = f.read().strip()
    raw_filesystem = expand(disk_map)
    defraged_filesystem = defrag(raw_filesystem)
    print(checksum(defraged_filesystem))


if __name__ == '__main__':
    main()