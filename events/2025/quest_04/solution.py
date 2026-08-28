from math import ceil, prod

def parse_input(data):
    return list(map(int, data.splitlines()))

def part_1(data):
    data = parse_input(data)
    return 2025 * data[0] // data[-1] 

def part_2(data):
    data = parse_input(data)
    return ceil(10000000000000 * data[-1] / data[0])

def part_3(data):
    data = [x.splitlines() for x in data.split("|")]
    return int(prod([int(x) / int(y) for x, y in data]) * 100)
      