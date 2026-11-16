def parse_input(data):
  return [line.split(":")[1] for line in data.splitlines()]

def part_1(data):
    data = parse_input(data)
    return sum(x == y for x, y in zip(data[0], data[2])) * sum(x == y for x, y in zip(data[1], data[2]))

def part_2(data):
    data = parse_input(data)
    res = 0
    for i in range(len(data)):
      for j in range(i + 1, len(data)):
        for k in range(len(data)):
          if k == i or k == j: continue
          a, b, c = data[i], data[j], data[k]
          if all(x == z or y == z for x, y, z in zip(a, b, c)):
            res += sum(x == y for x, y in zip(a, c)) * sum(x == y for x, y in zip(b, c))
            
    return res

def part_3(data):
    data = parse_input(data)
    return data
