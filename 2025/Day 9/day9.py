def part1():
    with open("input.txt") as f:
        lines = [line.strip() for line in f]
    res = 0
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            x1, y1 = map(int, lines[i].split(","))
            x2, y2 = map(int, lines[j].split(","))
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > res:
                res = area
    return res

print(part1())

def part2():
    # Read points (given sequentially forming the loop)
    with open("input.txt") as f:
        reds = [tuple(map(int, line.split(","))) for line in f]

    # Extract X and Y sets for coordinate compression
    xs = set(r[0] for r in reds)
    ys = set(r[1] for r in reds)

    # Add a margin around the polygon so we have a clear "outside" region
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    xs.add(min_x - 1)
    xs.add(max_x + 1)
    ys.add(min_y - 1)
    ys.add(max_y + 1)

    xs = sorted(xs)
    ys = sorted(ys)

    # Expand coords so interior strips exist
    cx = []
    for x in xs:
        cx.append(x)
        cx.append(x + 0.5)
    cy = []
    for y in ys:
        cy.append(y)
        cy.append(y + 0.5)

    cx = sorted(set(cx))
    cy = sorted(set(cy))

    x_to_ix = {v: i for i, v in enumerate(cx)}
    y_to_iy = {v: i for i, v in enumerate(cy)}

    W = len(cx)
    H = len(cy)

    # Allowed grid = 0 initially
    allowed = [[0] * W for _ in range(H)]

    # Mark boundary (green + red edges)
    n = len(reds)
    for i in range(n):
        x1, y1 = reds[i]
        x2, y2 = reds[(i + 1) % n]   # wrap
        if x1 == x2:
            ix = x_to_ix[x1]
            iy1 = y_to_iy[y1]
            iy2 = y_to_iy[y2]
            for iy in range(min(iy1, iy2), max(iy1, iy2) + 1):
                allowed[iy][ix] = 1
        else:
            iy = y_to_iy[y1]
            ix1 = x_to_ix[x1]
            ix2 = x_to_ix[x2]
            for ix in range(min(ix1, ix2), max(ix1, ix2) + 1):
                allowed[iy][ix] = 1

    # Flood fill OUTSIDE region
    from collections import deque
    q = deque()
    outside = [[False] * W for _ in range(H)]

    # Start from a guaranteed-outside coordinate: (min_x-1, min_y-1)
    start_ix = x_to_ix[min_x - 1]
    start_iy = y_to_iy[min_y - 1]
    q.append((start_iy, start_ix))
    outside[start_iy][start_ix] = True

    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and not outside[ny][nx] and allowed[ny][nx] == 0:
                outside[ny][nx] = True
                q.append((ny, nx))

    # All not-outside and not-boundary are INSIDE green tiles
    for y in range(H):
        for x in range(W):
            if allowed[y][x] == 0 and not outside[y][x]:
                allowed[y][x] = 1  # interior green

    # Build prefix sum of BLOCKED cells
    blocked = [[0] * (W + 1) for _ in range(H + 1)]
    for y in range(H):
        for x in range(W):
            b = 0 if allowed[y][x] else 1
            blocked[y + 1][x + 1] = (
                blocked[y][x + 1]
                + blocked[y + 1][x]
                - blocked[y][x]
                + b
            )

    def blocked_rect(x1, y1, x2, y2):
        return (
            blocked[y2 + 1][x2 + 1]
            - blocked[y1][x2 + 1]
            - blocked[y2 + 1][x1]
            + blocked[y1][x1]
        )

    # Try all pairs of red opposite corners
    best = 0
    for i in range(len(reds)):
        for j in range(i + 1, len(reds)):
            x1, y1 = reds[i]
            x2, y2 = reds[j]
            if x1 == x2 or y1 == y2:
                continue  # line, no area

            ix1, iy1 = x_to_ix[x1], y_to_iy[y1]
            ix2, iy2 = x_to_ix[x2], y_to_iy[y2]
            cx1, cx2 = sorted([ix1, ix2])
            cy1, cy2 = sorted([iy1, iy2])

            # Rectangle must only have allowed tiles
            if blocked_rect(cx1, cy1, cx2, cy2) != 0:
                continue

            # compute real tile area (original coordinates)
            w = abs(x1 - x2) + 1
            h = abs(y1 - y2) + 1
            best = max(best, w * h)

    return best

print(part2())