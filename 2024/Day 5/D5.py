f1 = open("2024\Day 5\D5_first_input.txt", "r")
f2 = open("2024\Day 5\D5_second_input.txt", "r")

rules = f1.readlines()
rules = [x.rstrip('\n') for x in rules]

updates = f2.readlines()
updates = [x.rstrip('\n') for x in updates]

def switch_place(page_list, a, b):
    temp = page_list[a]
    page_list[a] = page_list[b]
    page_list[b] = temp

    return page_list

rule_dict = {}
for rule in rules:
    pair = rule.split('|')
    if pair[0] not in rule_dict:
        rule_dict[pair[0]] = []
    rule_dict[pair[0]].append(pair[1])

def check_funct(page_list):

    wrong_pairs = []
    for i in range(0, len(page_list)):
        page = page_list[i]
        for n in range(0, i):
            if page in rule_dict and page_list[n] in rule_dict[page]:
                wrong_pairs.append([page, page_list[n]])

    if len(wrong_pairs) > 0:
        for pair in wrong_pairs:
                page_list = switch_place(page_list, page_list.index(pair[0]), page_list.index(pair[1]))

        check_funct(page_list)

res_1 = 0
res_2 = 0
for update in updates:
    valid = True
    page_list = update.split(',')
    mid_index = int((len(page_list) - 1)/2)
    mid_elem = page_list[mid_index]
    wrong_pairs = []

    for i in range(0, len(page_list)):
        page = page_list[i]
        for n in range(0, i):
            if page in rule_dict and page_list[n] in rule_dict[page]:
                valid = False
                wrong_pairs.append([page, page_list[n]])
    
    if valid:
        res_1 += int(mid_elem)
    else:
        for pair in wrong_pairs:
            page_list = switch_place(page_list, page_list.index(pair[0]), page_list.index(pair[1]))
        check_funct(page_list)
        res_2 += int(page_list[mid_index])

print("Part 1 answer: " + str(res_1))
print("Part 2 answer: " + str(res_2))