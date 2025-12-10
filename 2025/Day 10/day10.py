def part1():
    with open("test.txt") as f:
        lines = [line.strip().split(' ') for line in f]

    res = 0
    
    for line in lines:
        min = -1
        end = line[0]
        buttons = [[int(i) for i in x[1:-1].split(',')] for x in line[1:-1]]
        for mask in range(1 << len(buttons)):
            start = ["." for c in end[1:-1]]
            for i, btn in enumerate(buttons):
                if mask & (1 << i):
                    for pos in btn:
                        if start[pos] == '.':
                            start[pos] = '#'
                        else:
                            start[pos] = '.'

            if "".join(start) == end[1:-1]:
                if min == -1 or bin(mask).count('1') < min:
                    min = bin(mask).count('1')
        res += min

    return res


print(part1())

from collections import deque

def part2():
    with open("test.txt") as f:
        lines = [line.strip().split(' ') for line in f]

    res = 0
    
    for line in lines:
        end = tuple(int(x) for x in line[-1][1:-1].split(','))
        n = len(end)

        buttons = [tuple(int(x) for x in btn[1:-1].split(',')) for btn in line[1:-1]]

        start = tuple(0 for _ in range(n))
        q = deque([(start, 0)])
        visited = {start}

        while q:
            s, p = q.popleft()
            print(s, p)

            if s == end:
                res += p
                break

            # Expand BFS
            for btn in buttons:
                new_s = list(s)
                valid = True

                for i in btn:
                    new_s[i] += 1
                    if new_s[i] > end[i]:
                        valid = False
                        break

                if not valid:
                    continue

                new_s = tuple(new_s)
                if new_s not in visited:
                    visited.add(new_s)
                    q.append((new_s, p + 1))

    return res


print(part2())