import sys

def check(x,y,a):
    p_x = 3*(x//3)
    p_y = 3*(y//3)
    # 가로, 세로
    for i in range(9):
        if arr[x][i] == a or arr[i][y] == a:
            return False

    # 3x3
    for p in range(3):
        for k in range(3):
            if arr[p_x+p][p_y+k] == a:
                return False
    arr[x][y] = a
    return True


def bt(s):
    if s == len(zero_index_list):
        for i in range(9):
            print(*arr[i])
        exit(0)
    else:
        x,y = zero_index_list[s]
        for a in range(1,10):
            if check(x,y,a):
                bt(s+1)
                arr[x][y] = 0

arr = []
zero_index_list = []
for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if arr[i][j] == 0:
            zero_index_list.append((i,j))

bt(0)
