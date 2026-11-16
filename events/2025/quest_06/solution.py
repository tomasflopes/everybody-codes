from collections import defaultdict


def part_1(data):
    d = defaultdict(int)
    res = 0
    for c in data:
      if c.isupper():
        d[c] += 1
      elif c == 'a':
        res += d["A"]
    return res

def part_2(data):
    d = defaultdict(int)
    res = 0
    for c in data:
      if c.isupper():
        d[c] += 1
      elif c.islower():
        res += d[c.upper()]
    return res

def part_3(data):
    return data
      