def dfs(adj, node):
    if node == "out":
        return 1
    res = 0
    outputs = adj[node]
    for out in outputs:
        res += dfs(adj, out)

    return res

def part1():
    with open("input.txt") as f:
        lines = [[x.strip() for x in line.strip().split(':')] for line in f]
    
    adj = {}
    for line in lines:
        adj[line[0]] = [x for x in line[1].split(' ') if x]

    return dfs(adj, "you")


print(part1())

def dfs_p2(adj, node, dac, fft, memo):
    key = (node, dac, fft)
    if key in memo:
        return memo[key]
        
    if node == "out":
        memo[key] = 1 if (dac and fft) else 0
        return memo[key]
        
    new_dac = dac or (node == "dac")
    new_fft = fft or (node == "fft")
    
    res = 0
    outputs = adj[node]
    for out in outputs:
        res += dfs_p2(adj, out, new_dac, new_fft, memo)

    memo[key] = res
    return res

def part2():
    with open("input.txt") as f:
        lines = [[x.strip() for x in line.strip().split(':')] for line in f]
    
    adj = {}
    for line in lines:
        adj[line[0]] = [x for x in line[1].split(' ') if x]

    memo = {}
    return dfs_p2(adj, "svr", False, False, memo)


print(part2())