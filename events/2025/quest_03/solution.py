def parse_input(data):
    return list(map(int, data.split(",")))

def part_1(data):
    data = set(parse_input(data))
    return sum(data)

def part_2(data):
    data = sorted(set(parse_input(data)))
    return sum(data[:20])

def part_3(data):
    data = parse_input(data)
    counts = {}
    for x in data:
      counts[x] = counts.get(x, 0) + 1
    return max(counts.values())
