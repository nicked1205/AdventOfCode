f = open("2024\Day 6\D6_input.txt", "r")

grid = [[y for y in x.rstrip('\n')] for x in f.readlines()]
init_grid = [x.copy() for x in grid]

def locate_guard_init(grid):
    for x in range(0, len(grid)):
        if '^' in grid[x]:
            return x, grid[x].index('^')

def move_up(x, y, part1):
    if grid[x - 1][y] == '#':
        grid[x][y] = '>'
        return not (y == width - 1), x, y
    else:
        grid[x][y] = 'X'
        if not part1:
            grid[x][y] = 'W'
        grid[x - 1][y] = '^'
        x -= 1
        return not (x == 0), x, y
    
def move_down(x, y, part1):
    if grid[x + 1][y] == '#':
        grid[x][y] = '<'
        return not (y == 0), x, y
    else:
        grid[x][y] = 'X'
        if not part1:
            grid[x][y] = 'S'
        grid[x + 1][y] = 'v'
        x += 1
        return not (x == length - 1), x, y
    
def move_left(x, y, part1):
    if grid[x][y - 1] == '#':
        grid[x][y] = '^'
        return not (x == 0), x, y
    else:
        grid[x][y] = 'X'
        if not part1:
            grid[x][y] = 'A'
        grid[x][y - 1] = '<'
        y -= 1
        return not (y == 0), x , y
    
def move_right(x, y, part1):
    if grid[x][y + 1] == '#':
        grid[x][y] = 'v'
        return not (x == length - 1), x, y
    else:
        grid[x][y] = 'X'
        if not part1:
            grid[x][y] = 'D'
        grid[x][y + 1] = '>'
        y += 1
        return not (y == width - 1), x, y
    
def move(x, y, part1):
    if grid[x][y] == '^':
        movable, a, b = move_up(x, y, part1)
        return movable, a, b, not (grid[x - 1][y] == 'W')
    if grid[x][y] == '>':
        movable, a, b = move_right(x, y, part1)
        return movable, a, b, not (grid[x][y + 1] == 'D')
    if grid[x][y] == 'v':
        movable, a, b = move_down(x, y, part1)
        return movable, a, b, not (grid[x + 1][y] == 'S')
    if grid[x][y] == '<':
        movable, a, b = move_left(x, y, part1)
        return movable, a, b, not (grid[x][y - 1] == 'A')
    
def visualize(g):
    return "\n".join(["".join(x) for x in g])

def count_visited(grid):
    count = 0
    for x in range(length):
        for y in range(width):
            if grid[x][y] == 'X':
                count += 1
    return count
    
x, y = locate_guard_init(grid)
init_x, init_y = x, y
length = len(grid)
width = len(grid[0])

movable = True
while movable:
    movable, x, y, _ = move(x, y, True)
    # print(visualize(grid) + '\n')

grid[x][y] = 'X'
# print(visualize(grid) + '\n')

print("Part 1 answer: " + str(count_visited(grid)))
count = 0
for i in range(length):
    for j in range(width):
        grid = [x.copy() for x in init_grid]
        x, y = init_x, init_y
        if grid[i][j] == '.':
            grid[i][j] = '#'
        else:
            continue
        movable2 = True
        moves = 0
        while movable2:
            movable2, x, y, looped = move(x, y, False)
            moves += 1
            if moves > 9999:
                count += 1
                break

print("Part 2 answer: " + str(count))