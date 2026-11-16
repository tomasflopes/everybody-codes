from collections import defaultdict
import re


def part_1(data: str) -> str:
    p = defaultdict(int)
    for line in data.splitlines():
        match = re.match(r"id=(\d+) quest=(\d+) part=(\d+) time=(\d+)", line)
        id, _, _, time = map(int, match.groups())
        p[id] += time

    res = sum((i + 1) * t for i, t in enumerate(sorted(p.values())))

    return res


def part_2(data: str) -> str:
    p = defaultdict(lambda: [set(), 0])
    for line in data.splitlines():
        match = re.match(r"id=(\d+) quest=(\d+) part=(\d+) time=(\d+)", line)
        id, quest, part, time = map(int, match.groups())
        p[id][0].add((quest, part))
        p[id][1] += time

    p = sorted(p.values(), key=lambda entry: (-len(entry[0]), entry[1]))
    res = sum((i + 1) * t for i, (_, t) in enumerate(p))

    return res


def part_3(data: str) -> str:
    return ""


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
