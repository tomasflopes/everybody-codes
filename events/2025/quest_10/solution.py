N = 4
MOVES = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

def parse_input(data):
  return [line.strip() for line in data.splitlines()]

def print_board(data, dragons):
  print()
  for i, line in enumerate(data):
    for j, c in enumerate(line):
      print("X" if (i, j) in dragons else ".", end="")
    print()

def find_initial_dragon(data):
  for i, line in enumerate(data):
    for j, c in enumerate(line):
      if c == "D": return i, j

def find_sheep(data):
  s = set()
  for i, line in enumerate(data):
    for j, c in enumerate(line):
      if c == "S": s.add((i, j))
  return s

def move(dragon, data):
  s = set()
  x, y = dragon
  for dx, dy in MOVES:
    if 0 <= x + dx < len(data) or 0 <= y + dy < len(data[0]): s.add((x+dx, y+dy))
  return s

def part_1(data):
    data = parse_input(data)
    dragon_pos = find_initial_dragon(data)
    sheep = find_sheep(data)
    dragons = set()
    dragons.add(dragon_pos)
    for _ in range(N):
      t = set()
      for dragon in dragons:
        t |= move(dragon, data)
      dragons |= t
      # print_board(data, dragons)

    return len(sheep & dragons)

def part_2(data):
    data = parse_input(data)
    return data

def part_3(data):
    data = parse_input(data)
    return data
