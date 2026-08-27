def parse_input(data):
    lines = data.strip().splitlines()
    return lines[0].split(","), lines[2].split(",")

def solve(names, res, move, wrap):
    step = (-1 if move[0] == "L" else 1) * int(move[1:])
    i = names.index(res)
    delta = (i + step) % len(names) if wrap else min(max(i + step, 0), len(names) - 1)

    return names[delta]

def part_1(data):
    names, moves = parse_input(data)
    res = names[0]
    for move in moves:
        res = solve(names, res, move, wrap=False)
    return res

def part_2(data):
    names, moves = parse_input(data)
    res = names[0]
    for move in moves:
        res = solve(names, res, move, wrap=True)
    return res

def part_3(data):
    names, moves = parse_input(data)
    for move in moves:
        step = ((-1 if move[0] == "L" else 1) * int(move[1:])) % len(names)
        names[0], names[step] = names[step], names[0]
    return names[0]
