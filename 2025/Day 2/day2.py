def part1():
    f = open("input.txt", "r")
    line = f.readline()
    ranges = line.strip().split(",")

    res = 0

    for r in ranges:
        start, end = map(str, r.split("-"))

        for num in range(int(start), int(end) + 1):
            l = len(str(num))

            if l % 2 != 0:
                continue

            pre = str(num)[:l//2]
            suf = str(num)[l//2:]

            if pre == suf:
                # print(pre + pre)
                res += int(pre + pre)
    
    return res

print(part1())

def part2():
    f = open("input.txt", "r")
    line = f.readline()
    ranges = line.strip().split(",")

    res = 0

    for r in ranges:
        start, end = map(str, r.split("-"))

        for num in range(int(start), int(end) + 1):
            l = len(str(num))

            for div in range(2, l + 1):
                if l % div != 0:
                    continue

                unit = l // div

                s = 0
                e = l // div

                while e <= l:
                    pre = str(num)[s:e]
                    suf = str(num)[e:e + unit]

                    if pre != suf:
                        break

                    s += unit
                    e += unit
                
                if e >= l:
                    # print(pre * div)
                    res += int(pre * div)
                    break
    
    return res

print(part2())