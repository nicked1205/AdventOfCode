class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_sizes(self):
        roots = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            roots[r] = roots.get(r, 0) + 1
        return sorted(roots.values(), reverse=True)

import heapq, math

def part1(filename, merge_k):
    with open(filename) as f:
        coords = [tuple(map(int, s.split(","))) for s in f]

    n = len(coords)
    dsu = DSU(n)
    heap = []

    # Build min-heap of squared distances
    for i in range(n):
        x1, y1, z1 = coords[i]
        for j in range(i+1, n):
            x2, y2, z2 = coords[j]
            dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2  # squared only
            heap.append((dist, i, j))
    heapq.heapify(heap)

    # Perform K "connections"
    for _ in range(merge_k):
        _, a, b = heapq.heappop(heap)
        dsu.union(a, b)  # may merge, may do nothing (still counts)

    sizes = dsu.component_sizes()
    return sizes[0] * sizes[1] * sizes[2]

def part2(filename):
    with open(filename) as f:
        coords = [tuple(map(int, s.split(","))) for s in f]

    n = len(coords)
    dsu = DSU(n)
    heap = []

    # Build min-heap of squared distances
    for i in range(n):
        x1, y1, z1 = coords[i]
        for j in range(i+1, n):
            x2, y2, z2 = coords[j]
            dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
            heap.append((dist, i, j))
    heapq.heapify(heap)

    # Merge until fully connected: one component remains
    while heap:
        _, a, b = heapq.heappop(heap)
        if dsu.union(a, b):
            if dsu.size[dsu.find(a)] == n:  # fully connected
                x1, _, _ = coords[a]
                x2, _, _ = coords[b]
                return x1 * x2   # multiply X-values only

print(part1("input.txt", 1000))
print(part2("input.txt"))
