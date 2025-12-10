from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatusOptimal
import re

def parse_line(line):
    parts = line.strip().split()
    # Parse target like {3,5,4,7}
    target = tuple(int(x) for x in parts[-1][1:-1].split(','))
    # Parse buttons like (1,3,4)
    buttons = [tuple(int(x) for x in p[1:-1].split(',')) for p in parts[1:-1]]
    return target, buttons

def solve_machine(target, buttons):
    m = len(buttons)
    n = len(target)

    # Setup ILP
    prob = LpProblem("JoltageMachine", LpMinimize)
    
    # Integer press counts
    x = [LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(m)]

    # Constraints for each counter
    for i in range(n):
        prob += lpSum(x[j] for j, btn in enumerate(buttons) if i in btn) == target[i]

    # Minimize total presses
    prob += lpSum(x)

    # Solve
    status = prob.solve()
    if status != 1:  # LpStatusOptimal
        raise RuntimeError("Unexpected: Machine has no solution but input assumed solvable.")
    
    # Sum presses
    presses = sum(int(v.value()) for v in x)
    return presses

def part2():
    total = 0
    with open("input.txt") as f:
        for line in f:
            target, buttons = parse_line(line)
            total += solve_machine(target, buttons)
    return total

print(part2())