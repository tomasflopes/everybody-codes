from math import ceil, sqrt


def part_1(data: str) -> str:
  data = list(map(int, data.split(",")))
  res = 0
  for x in data:
    s = pow(ceil(sqrt(x)), 2)
    res += s - x
  return res


def part_2(data: str) -> str:
  data = list(map(int, data.split(",")))
  res = 0
  for x in data:
    side = ceil(sqrt(x)) if x > 8 else 3
    p = side * 4 - 4
    while p < x: 
      side += 1
      p = side * 4 - 4
    res += p - x
  return res


def part_3(data: str) -> str:
  data = list(map(int, data.split(",")))
  res = 0
  for x in data:
    s = (pow(ceil(sqrt(x)), 2) if ceil(sqrt(x)) % 2 == 1 else pow(ceil(sqrt(x))+1, 2)) if x > 8 else 9
    res += s - 1 - x if s > x else pow(ceil(sqrt(x) + 2), 2) - 1 -x
  return res


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
