import re

test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test_input2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

f = open("2024\Day 3\D3_input.txt", "r")
inp = f.read()

def calculate(inp):
    matches = re.findall("mul\([1-9][0-9]*,[1-9][0-9]*\)", inp)

    pairs = [ x[4:-1] for x in matches ]

    sum = 0
    for pair in pairs:
        nums = pair.split(',')
        sum += int(nums[0]) * int(nums[1])
    return sum

print ("Part 1 answer: " + str(calculate(inp)))

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

matches = re.findall(pattern, inp)

answer_2 = 0
enabled = True

for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    else:
        if enabled:
            x, y = map(int, match[4:-1].split(","))
            answer_2 += x * y 

print ("Part 2 answer: " + str(answer_2))