N = 3
MOVES = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

def parse_input(data):
  return [line.strip() for line in data.splitlines()]

def print_board(data, dragons, sheep):
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

def move_dragon(dragon, data):
  s = set()
  x, y = dragon
  for dx, dy in MOVES:
    if 0 <= x + dx < len(data) or 0 <= y + dy < len(data[0]): s.add((x+dx, y+dy))
  return s

def move_sheep(sheep, data):
  x, y = sheep
  if x + 1 >= len(data): return None
  return x+1, y

def eat_sheep(sheep, dragons, data):
  s = set(sheep)
  for i, line in enumerate(data):
    for j, c in enumerate(line):
      if c != "#" and (i, j) in sheep and (i, j) in dragons: 
        print(i, j)
        s.remove((i, j))

  print(len(sheep) - len(s))
  return s, len(sheep) - len(s)

def part_1(data):
    data = parse_input(data)
    dragon_pos = find_initial_dragon(data)
    sheep = find_sheep(data)
    dragons = set()
    dragons.add(dragon_pos)
    for _ in range(N):
      t = set()
      for dragon in dragons:
        t |= move_dragon(dragon, data)
      dragons |= t
      # print_board(data, dragons, sheep)

    return len(sheep & dragons)

def part_2(data):
    data = parse_input(data)
    dragon_pos = find_initial_dragon(data)
    sheep = find_sheep(data)
    dragons = set()
    dragons.add(dragon_pos)
    res = 0
    for i in range(N):
      t = set()
      s = set()
      for dragon in dragons:
        t |= move_dragon(dragon, data)
      dragons |= t
      if i == 0:
        dragons.remove(dragon_pos)

      sheep, acc = eat_sheep(sheep, dragons, data)
      res += acc
      for ss in sheep:
        pos = move_sheep(ss, data)
        if pos != None: s.add(pos)
      print_board(data, dragons, sheep)
      res += acc

    return res
    # 322 wrong

def part_3(data):
    data = parse_input(data)
    return data
