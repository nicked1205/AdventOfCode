def part1():
    f = open("input.txt", "r")
    cur = 50
    count = 0
    for line in f:
        dir = line[0]
        val = int(line[1:])
        cur = cur + val if dir == 'R' else cur - val

        if cur % 100 == 0:
            count += 1
    
    return count

print(part1())

def part2():
    f = open("input.txt", "r")
    cur = 50
    count = 0
    prev0 = False
    for line in f:
        dir = line[0]
        val = int(line[1:])
        cur = cur + val if dir == 'R' else cur - val
        
        if cur < 0:
            count += int(abs(cur) / 100)
            count += 1 if not prev0 else 0
            cur = 100 - (abs(cur) % 100)
            if cur == 100:
                cur = 0
        elif cur > 99:
            count += int(cur / 100)
            cur %= 100
        elif cur == 0:
            count += 1 if not prev0 else 0

        if cur % 100 == 0:
            prev0 = True
        else:
            prev0 = False

        print(dir, val, cur, count)
    
    return count

print(part2())