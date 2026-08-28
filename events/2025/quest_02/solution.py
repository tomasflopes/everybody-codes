import re

def parse_input(data):
    x, y = tuple(map(int, re.findall(r"-?\d+", data)))
    return x + y * 1j

def apply_cycle(r, a, d):
    r *= r
    r = int(r.real / d) + int(r.imag / d) * 1j
    return r + a

def part_1(data):
    a = parse_input(data)
    r = 0
    for _ in range(3):
        r = apply_cycle(r, a, 10)
    return f"[{int(r.real)},{int(r.imag)}]"


def part_2(data):
    bound = 1000000
    a = parse_input(data)
    res = 0

    for r in range(101):
      for i in range(101):
        p = (a.real + r * 10) + (a.imag + i * 10) * 1j
        n = 0
        for _ in range(100):
          n = apply_cycle(n, p, 100000)
          if -bound <= n.real <= bound and -bound <= n.imag <= bound:
            continue
          break
        else:
          res += 1
    return res

def part_3(data):
    bound = 1000000
    a = parse_input(data)
    res = 0

    for r in range(1001):
      for i in range(1001):
        p = (a.real + r) + (a.imag + i) * 1j
        n = 0
        for _ in range(100):
          n = apply_cycle(n, p, 100000)
          if -bound <= n.real <= bound and -bound <= n.imag <= bound:
            continue
          break
        else:
          res += 1
    return res
