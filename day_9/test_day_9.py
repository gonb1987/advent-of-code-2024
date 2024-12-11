from main import expand, compact, checksum, defrag


disk_map = '2333133121414131402'


def test_expand():
    assert expand(disk_map) == list('00...111...2...333.44.5555.6666.777.888899')

def test_compact():
    assert compact(
        list('00...111...2...333.44.5555.6666.777.888899')) == list('0099811188827773336446555566..............')

def test_checksum():
    assert checksum(list('0099811188827773336446555566..............')) == 1928

def test_defrag():
    assert defrag(list('00...111...2...333.44.5555.6666.777.888899')) == list('00992111777.44.333....5555.6666.....8888..')