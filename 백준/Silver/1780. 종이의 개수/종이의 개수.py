import sys

def check(x,y,arr_len):
    point = arr[y][x]
    for i in range(y,y+arr_len):
        for j in range(x,x+arr_len):
            if not point == arr[i][j]:
                return False
    return True

def paper(x,y,arr_len):
    global res_minus_one , res_plus_one, res_zero
    if check(x,y,arr_len) or arr_len == 1:
        if arr[y][x] == -1:
           res_minus_one += 1
        elif arr[y][x] == 1:
           res_plus_one += 1
        else:
            res_zero += 1
    else:
        arr_len //= 3
        for i in range(3):
            for j in range(3):
                paper(x+(arr_len*i),y+(arr_len*j),arr_len)
        
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
res_minus_one = 0
res_plus_one = 0
res_zero = 0
paper(0,0,len(arr))
print(res_minus_one)
print(res_zero)
print(res_plus_one)
