def part1():
    f = open("input.txt", "r")
    beams = set()
    count = 0
    for line in f:
        line = line.strip()
        for i in range(len(line)):
            if line[i] == 'S':
                beams.add(i)
            if line[i] == '^' and i in beams:
                beams.remove(i)
                count+=1
                if i - 1 >= 0:
                    beams.add(i - 1)
                if i + 1 < len(line):
                    beams.add(i + 1)
    return count

print(part1())

def dfs(x, y, grid, memo):
    if y < 0 or y >= len(grid[0]):
        return 0

    if x == len(grid) - 1:
        return 1

    if (x, y) in memo:
        return memo[(x, y)]

    total = 0

    if grid[x][y] == '^':
        total += dfs(x + 1, y + 1, grid, memo)
        total += dfs(x + 1, y - 1, grid, memo)
    else:
        total += dfs(x + 1, y, grid, memo)

    memo[(x, y)] = total
    return total

def part2():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    start_col = lines[0].index('S')
    return dfs(1, start_col, lines, {})

print(part2())