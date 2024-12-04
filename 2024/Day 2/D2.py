f = open("2024\Day 2\D2_input.txt", "r")
        

def test_data(values, possible_subtraction):
    res = True
    for i in range (1, len(values) - 1):
        if (values[i] - values[i + 1]) not in possible_subtraction:
            res = False
    
    return res

def test_function(arr):
    inc_subtraction_res = [-1, -2, -3]
    dec_subtraction_res = [1, 2, 3]
    return ((arr[0] - arr[1]) in inc_subtraction_res and test_data(arr, inc_subtraction_res)) or ((arr[0] - arr[1]) in dec_subtraction_res and test_data(arr, dec_subtraction_res))

safe_count_1 = 0
safe_count_2 = 0
for line in f:
    values = line.rstrip('\n').split(" ")
    int_values = [int(x) for x in values]
    if test_function(int_values):
        safe_count_1 += 1
        safe_count_2 += 1
    else:
        safe = False
        for i in range(0, len(int_values)):
            new_list = int_values.copy()
            new_list.pop(i)
            if test_function(new_list):
                safe = True
        if safe:
            safe_count_2 += 1


print ("Part 1 answer: " + str(safe_count_1))
print ("Part 2 answer: " + str(safe_count_2))