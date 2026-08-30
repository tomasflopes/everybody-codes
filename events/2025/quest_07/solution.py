def parse_input(data):
    names, rules = data.split("\n\n")
    rules = rules.splitlines()
    m = {}
    for r in rules:
      b, a = r.split(">")
      m[b.strip()] = [x.strip() for x in a.split(",")]
    return names.split(","), m

def part_1(data):
    names, rules = parse_input(data)
    for name in names:
      for i in range(len(name) - 1):
        if not name[i+1] in rules[name[i]]:
          break
      else:
        return name

def part_2(data):
    names, rules = parse_input(data)
    res = 0
    for j, name in enumerate(names):
      for i in range(len(name) - 1):
        if not name[i+1] in rules[name[i]]:
          break
      else:
        res += j + 1
    return res

def find_combinations(name, rules):
  names = set()
  if len(name) >= 7: names.add(name)
  if len(name) >= 11: return names

  for r in rules.get(name[-1], []):
    names |= find_combinations(name + r, rules)

  return names

def part_3(data):
    names, rules = parse_input(data)
    p = set()
    for name in names:
      for i in range(len(name) - 1):
        if not name[i+1] in rules[name[i]]:
          break
      else:
        p |= find_combinations(name, rules)

    return len(p)
      