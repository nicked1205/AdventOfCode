def part1():
    f = open("input.txt", "r")
    ranges = []
    res = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break

        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    for line in f:
        line = line.strip()
        num = int(line)
        for start, end in ranges:
            if start <= num <= end:
                res+=1
                break

    return res

print(part1())

def part2():
    f = open("input.txt", "r")
    ranges = []
    res = 0
    for line in f:
        line = line.strip()
        print(line)
        if len(line) == 0:
            break

        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    ranges.sort()

    merged = []
    current_start, current_end = ranges[0]

    for s, e in ranges[1:]:
        if s <= current_end:
            current_end = max(current_end, e)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = s, e

    merged.append((current_start, current_end))

    res = sum(e - s + 1 for s, e in merged)
    return res

print(part2())