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
    times = defaultdict(dict)
    participant_ids = set()

    for line in data.splitlines():
        match = re.match(r"id=(\d+) quest=(\d+) part=(\d+) time=(\d+)", line)
        participant_id, quest, part, time = map(int, match.groups())
        participant_ids.add(participant_id)
        times[(quest, participant_id)][part] = time

    quests = sorted({quest for quest, _ in times})
    points = defaultdict(int)

    for quest in quests:
        for part in range(1, 4):
            completed = []
            for participant_id in participant_ids:
                participant_times = times[(quest, participant_id)]
                if all(current_part in participant_times for current_part in range(1, part + 1)):
                    combined_time = sum(
                        participant_times[current_part]
                        for current_part in range(1, part + 1)
                    )
                    completed.append((combined_time, participant_id))

            completed.sort(key=lambda entry: entry[0])
            position = 1
            previous_time = None
            for index, (combined_time, participant_id) in enumerate(completed):
                if index == 0 or combined_time != previous_time:
                    position = index + 1
                awarded_points = max(50 * part - (position - 1), 0)
                points[participant_id] += awarded_points
                previous_time = combined_time

    ordered = sorted(
        ((participant_id, points[participant_id]) for participant_id in participant_ids),
        key=lambda entry: entry[1],
        reverse=True,
    )
    checksum = 0
    position = 1
    previous_score = None
    for index, (_, score) in enumerate(ordered):
        if index == 0 or score != previous_score:
            position = index + 1
        checksum += position * score
        previous_score = score

    return checksum


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
