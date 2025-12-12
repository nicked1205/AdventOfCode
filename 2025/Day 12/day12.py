def rotate(grid, k):
    k = k % 4
    for _ in range(k):
        grid = [list(row) for row in zip(*grid[::-1])]
    return grid

from collections import deque

def part1():
    with open("test.txt") as f:
        lines = [line.strip() for line in f]
    
    presents = []
    present = []
    readingPresent = True
    grids = []
    for line in lines:
        if readingPresent:
            if len(line) == 3:
                present.append(list(line))
            elif len(line) == 0:
                presents.append(present)
                present = []
        else:
            line = line.split(':')
            size = line[0]
            amounts = [int(x) for x in line[1].strip().split(' ')]
            grids.append((size, amounts))

        if len(presents) == 6:
            readingPresent = False

    allShapes = []
    for p in presents:
        shapes = []
        for rot in range(4):
            rotated = rotate(p, rot)
            shapes.append(rotated)
        allShapes.append(shapes)

    res = 0

    for s, a in grids:
        m, n = map(int, s.split('x'))
        grid = [['.' for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append((grid, a))

        while q:
            grid, amounts = q.popleft()
            print(m, n , amounts)
            if all(x == 0 for x in amounts):
                res += 1
                break

            for i in range(6):
                if amounts[i] == 0:
                    continue
                present = allShapes[i]
                for rot in range(4):
                    rotated = present[rot]
                    
                    for r in range(1, m - 1):
                        for c in range(1, n - 1):
                            canPlace = True
                            for pr in range(len(rotated)):
                                for pc in range(len(rotated[0])):
                                    if rotated[pr][pc] == '#':
                                        if r + pr >= m or c + pc >= n or grid[r + pr][c + pc] == '#':
                                            canPlace = False
                            if canPlace:
                                newGrid = [row[:] for row in grid]
                                for pr in range(len(rotated)):
                                    for pc in range(len(rotated[0])):
                                        if rotated[pr][pc] == '#':
                                            newGrid[r + pr][c + pc] = '#'
                                newAmounts = amounts[:]
                                newAmounts[i] -= 1
                                q.append((newGrid, newAmounts))
    return res


print(part1())