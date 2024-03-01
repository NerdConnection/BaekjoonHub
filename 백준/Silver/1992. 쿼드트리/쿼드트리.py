import sys

def check(arr, x, y, len_arr):
    point = arr[y][x]
    for i in range(y, y + len_arr):
        for j in range(x, x + len_arr):
            if point != arr[i][j]:
                return False
    return True

def tree(arr, x, y, len_arr):
    if check(arr, x, y, len_arr) or len_arr == 1:
        print(arr[y][x],end='')             
    else:                        
        print('(',end='')
        len_arr = len_arr // 2                                                                                                                           
        tree(arr, x, y, len_arr)
        tree(arr, x + len_arr, y, len_arr)
        tree(arr, x, y + len_arr, len_arr)
        tree(arr, x + len_arr, y + len_arr, len_arr)
        print(')',end='')

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,list(input().rstrip()))))

tree(arr,0,0,len(arr))