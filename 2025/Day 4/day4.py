from collections import deque

def check_adjacent(x, y, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '@':
                count+=1
    return count

def part1():
    f = open("input.txt", "r")
    res = 0
    grid = [line.strip() for line in f.readlines()]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                if check_adjacent(i, j, grid) < 4:
                    res += 1
    
    return res

print(part1())

def remove_rolls(grid):
    R, C = len(grid), len(grid[0])
    queue = deque()
    removed = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == '@' and check_adjacent(i, j, grid) < 4:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        
        if grid[x][y] != '@':
            continue
        
        grid[x][y] = 'x'
        removed += 1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '@':
                if check_adjacent(nx, ny, grid) < 4:
                    queue.append((nx, ny))

    return removed


def part2():
    f = open("input.txt", "r")
    grid = [list(line.strip()) for line in f.readlines()]
    
    res = remove_rolls(grid)
    
    return res

print(part2())