def parse_input(data):
  return list(map(int, data.split(",")))

NAILS = 8

def part_1(data):
    data = parse_input(data)
    res = 0
    for x, y in zip(data, data[1:]):
      res += 1 if abs(x - y) == NAILS // 2 else 0

    return res

def part_2(data):
    data = parse_input(data)
    return data

def part_3(data):
    data = parse_input(data)
    return data
