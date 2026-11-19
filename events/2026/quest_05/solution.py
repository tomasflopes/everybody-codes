DIRS = [(1, 1), (1, 0), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]

def attach(m, i, j):
    pending = {
        (i + dx, j + dy)
        for dx, dy in DIRS
        if 0 <= i + dx < len(m) and 0 <= j + dy < len(m[0])
    }

    while pending:
        i, j = pending.pop()
        if m[i][j] == 2:
            continue

        count = sum(
            0 <= i + dx < len(m)
            and 0 <= j + dy < len(m[0])
            and m[i + dx][j + dy] > 0
            for dx, dy in DIRS
        )

        if count < 5:
            continue

        m[i][j] = 2
        for dx, dy in DIRS:
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(m) and 0 <= nj < len(m[0]):
                pending.add((ni, nj))


def reconstruct(data):
    m = [[int(cell) for cell in line] for line in data.splitlines()]
    center = (len(m) // 2, len(m[0]) // 2)
    m[center[0]][center[1]] = 2
    attach(m, *center)
    return m


def part_1(data: str) -> str:
    m = reconstruct(data)
    return sum(cell == 2 for row in m for cell in row)
        

def part_2(data: str) -> str:
    m = reconstruct(data)
    height, width = len(m), len(m[0])
    pending = set()
    coastline = set()

    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            if cell != 2:
                continue
            if i in (0, height - 1) or j in (0, width - 1):
                coastline.add((i, j))
                continue
            if any(m[i + di][j + dj] != 2 for di, dj in DIRS):
                coastline.add((i, j))

    for i, j in coastline:
        m[i][j] = 3
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                pending.add((ni, nj))

    while pending:
        i, j = pending.pop()
        if m[i][j] != 2:
            continue

        count = sum(
            0 <= i + di < height
            and 0 <= j + dj < width
            and m[i + di][j + dj] == 3
            for di, dj in DIRS
        )
        if count < 5:
            continue

        m[i][j] = 3
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                pending.add((ni, nj))

    return sum(cell == 3 for row in m for cell in row)


def reconstruct_sand(data):
    m = reconstruct(data)
    height, width = len(m), len(m[0])
    coastline = set()

    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            if cell != 2:
                continue
            if i in (0, height - 1) or j in (0, width - 1):
                coastline.add((i, j))
                continue
            if any(m[i + di][j + dj] != 2 for di, dj in DIRS):
                coastline.add((i, j))

    pending = set()
    for i, j in coastline:
        m[i][j] = 3
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                pending.add((ni, nj))

    while pending:
        i, j = pending.pop()
        if m[i][j] != 2:
            continue

        count = sum(
            0 <= i + di < height
            and 0 <= j + dj < width
            and m[i + di][j + dj] == 3
            for di, dj in DIRS
        )
        if count < 5:
            continue

        m[i][j] = 3
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                pending.add((ni, nj))

    return m


def part_3(data: str) -> str:
    m = reconstruct_sand(data)
    height, width = len(m), len(m[0])

    stamp = (
        (-2, -1), (-2, 0), (-2, 1),
        (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
        (0, -2), (0, -1), (0, 1), (0, 2),
        (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
        (2, -1), (2, 0), (2, 1),
    )

    for i in range(height):
        for j in range(width):
            if m[i][j] != 2:
                continue

            if all(
                0 <= i + di < height
                and 0 <= j + dj < width
                and m[i + di][j + dj] in (2, 4)
                for di, dj in stamp
            ):
                m[i][j] = 4

    for _ in range(2):
        grown = set()
        for i in range(height):
            for j in range(width):
                if m[i][j] != 2:
                    continue

                neighbors = [
                    m[i + di][j + dj]
                    for di, dj in DIRS
                    if 0 <= i + di < height and 0 <= j + dj < width
                ]
                if (
                    3 not in neighbors
                    and sum(cell == 4 for cell in neighbors) >= 4
                ):
                    grown.add((i, j))

        for i, j in grown:
            m[i][j] = 4

    return str(sum(cell == 4 for row in m for cell in row))


def main() -> None:
    pass  # debugging


if __name__ == "__main__":
    main()
