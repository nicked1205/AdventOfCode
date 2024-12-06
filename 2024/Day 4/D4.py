f = open("2024\Day 4\D4_input.txt", "r")

wordsearch = f.readlines()
wordsearch = [x.rstrip('\n') for x in wordsearch]

def search_hor_vert(M_x, M_y, dir):
    res = False
    dir_int = 1
    if dir == 'L' or dir == 'U':
        dir_int = -1
    
    if (dir == 'L' or dir == 'R') and (wordsearch[M_x][M_y + dir_int] == 'A' and wordsearch[M_x][M_y + 2 * dir_int] == 'S'):
        res = True
    
    if (dir == 'U' or dir == 'D') and (wordsearch[M_x + dir_int][M_y] == 'A' and wordsearch[M_x + 2 * dir_int][M_y] == 'S'):
        res = True
    
    return res

def search_diag(M_x, M_y, dir):
    dir_x = 1
    dir_y = 1
    if dir == 'DL':
        dir_y = -1
    elif dir == 'UL':
        dir_x = -1
        dir_y = -1
    elif dir == 'UR':
        dir_x = -1

    if wordsearch[M_x + dir_x][M_y + dir_y] == 'A' and wordsearch[M_x + 2 * dir_x][M_y + 2 * dir_y] == 'S':
        return True
    
    return False

def search_X(X_x, X_y, length, height):
    count = 0
    
    if X_x <= height - 4:
        if wordsearch[X_x + 1][X_y] == 'M' and search_hor_vert(X_x + 1, X_y, 'D'):
            count += 1 

    if X_y <= length - 4:
        if wordsearch[X_x][X_y + 1] == 'M' and search_hor_vert(X_x, X_y + 1, 'R'):
            count += 1

    if X_x >= 3:
        if wordsearch[X_x - 1][X_y] == 'M' and search_hor_vert(X_x - 1, X_y, 'U'):
            count += 1

    if X_y >= 3:
        if wordsearch[X_x][X_y - 1] == 'M' and search_hor_vert(X_x, X_y - 1, 'L'):
            count += 1

    if X_x <= height - 4 and X_y <= length - 4:
        if wordsearch[X_x + 1][X_y + 1] == 'M' and search_diag(X_x + 1, X_y + 1, 'DR'):
            count += 1

    if X_x <= height - 4 and X_y >= 3:
        if wordsearch[X_x + 1][X_y - 1] == 'M' and search_diag(X_x + 1, X_y - 1, 'DL'):
            count += 1

    if X_x >= 3 and X_y <= length - 4:
        if wordsearch[X_x - 1][X_y + 1] == 'M' and search_diag(X_x - 1, X_y + 1, 'UR'):
            count += 1

    if X_x >= 3 and X_y >= 3:
        if wordsearch[X_x - 1][X_y - 1] == 'M' and search_diag(X_x - 1, X_y - 1, 'UL'):
            count += 1

    return count

def search_A(A_x, A_y, length, height):
    if A_x != height - 1 and A_x != 0 and A_y != height - 1 and A_y != 0:
        M_count = 0
        S_count = 0
        arr = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                if wordsearch[A_x + i][A_y + j] == 'M':
                    M_count += 1
                    arr.append('M')
                elif wordsearch[A_x + i][A_y + j] == 'S':
                    S_count += 1
                    arr.append('S')
        
        if (M_count == 2 and S_count == 2) and arr[0] != arr[3] and arr[1] != arr[2]:
            return True
        else: 
            return False
    return False

count = 0
count_2 = 0
for x in range(0, len(wordsearch)):
    for y in range(0, len(wordsearch[0])):
        if wordsearch[x][y] == 'X':
            count += search_X(x, y, len(wordsearch[0]), len(wordsearch))
        if wordsearch[x][y] == 'A' and search_A(x, y, len(wordsearch[0]), len(wordsearch)):
            count_2 += 1

print ("Part 1 answer: " + str(count))
print ("Part 2 answer: " + str(count_2))