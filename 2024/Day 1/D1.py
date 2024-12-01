f = open("2024\Day 1\D1_input.txt", "r")
l1 = []
l2 = []

for line in f:
    line = line.split("   ")
    l1.append(int(line[0]))
    l2.append (int(line[1].rstrip("\n")))
l1_sorted = sorted(l1)
l2_sorted = sorted(l2)

distance = 0
similarity = 0
for i in range(0, len(l1_sorted)):
    distance += abs(l1_sorted[i] - l2_sorted[i])
    similarity += l1_sorted[i] * l2_sorted.count(l1_sorted[i])

print ("Part 1 answer: " + str(distance))
print ("Part 2 answer: " + str(similarity))