from collections import defaultdict

def comparisons(data: str):
    for line in data.splitlines():
        harder = defaultdict(set)
        seen = set()
        for comparison in line.split():
            left, operator, right = comparison
            seen.update((left, right))
            if operator == "<":
                left, right = right, left
            harder[left].add(right)
        yield harder, seen


def part_1(data: str):
    total = 0

    for harder, seen in comparisons(data):
        order = sorted(seen, key=lambda alloy: len(harder[alloy]), reverse=True)
        total += int("".join(order))

    return total


def part_2(data: str):
    total = 0

    for harder, remaining in comparisons(data):
        order = []
        remaining = set(remaining)

        while remaining:
            candidates = [
                alloy for alloy in remaining
                if not any(alloy in harder[other] for other in remaining)
            ]
            order.append(candidates[0])
            remaining.remove(candidates[0])

        total += int("".join(order))

    return total

def part_3(data: str):
  return part_2(data)


if __name__ == "__main__":
    pass
