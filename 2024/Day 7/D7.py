def calculate(part2):
    f = open("2024\Day 7\D7_input.txt", "r")
    res = 0
    for line in f:
        line = line.rstrip('\n').split(" ")
        test_val = int(line[0][0:-1])
        op_vals = [int(x) for x in line[1:]]
        final_results = [op_vals[0]]
        for i in range(1, len(op_vals)):
            temp = []
            for num in final_results:
                sum = num + op_vals[i]
                if sum <= test_val:
                    temp.append(sum)

                mult = num * op_vals[i]
                if mult <= test_val:
                    temp.append(mult)
                if part2:
                    conc = int(str(num) + str(op_vals[i]))
                    if conc <= test_val:
                        temp.append(conc)
            final_results = temp.copy()
        if test_val in final_results:
            print('Add ' + str(test_val))
            res+= test_val
    return res

print("Part 1 answer: " + str(calculate(False)))
print("Part 2 answer: " + str(calculate(True)))