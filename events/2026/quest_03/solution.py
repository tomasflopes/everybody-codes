from math import ceil


def part_1(data: str) -> str:
    res = 0
    for line in data.splitlines():
      x, y = line.split()
      x = x.split("-")[1]
      n = 0
      for p, (i, j) in enumerate(zip(x, y)):
        i, j = int(i), int(j)
        power = len(x) - p - 1
        n += pow(i, power) * j

      res += n

    return res


def part_2(data: str) -> str:
    res = 0
    for line in data.splitlines():
      x, y = line.split()
      x = x.split("-")[1]
      n = 0
      x *= ceil(len(y) / len(x))
      x = x[-len(y):]
      for p, (i, j) in enumerate(zip(x, y)):
        i, j = int(i), int(j)
        power = len(x) - p - 1
        n += pow(i, power) * j

      res += n

    return res


def part_3(data: str) -> str:
    res = 0

    for line in data.splitlines():
      base, digits = line.split()
      base = base.split("-")[1]
      value = 0

      repeated_base = base * ceil(len(digits) / len(base))
      repeated_base = repeated_base[-len(digits):]
      for p, (i, j) in enumerate(zip(repeated_base, digits)):
        value += int(i) ** (len(digits) - p - 1) * int(j)

      valid = True
      for smaller in range(int(digits)):
        candidate = str(smaller)
        candidate_base = base * ceil(len(candidate) / len(base))
        candidate_base = candidate_base[-len(candidate):]
        candidate_value = sum(
          int(i) ** (len(candidate) - p - 1) * int(j)
          for p, (i, j) in enumerate(zip(candidate_base, candidate))
        )
        if candidate_value == value:
          valid = False
          break

      if valid:
        res += value

    return res


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
