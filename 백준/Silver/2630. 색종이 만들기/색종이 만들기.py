import sys

def check(arr, start_x, start_y, length_arr):
    global blue , white
    point = arr[start_y][start_x]
    if length_arr == 1:
        if point == 1:
            blue += 1
        else:
            white += 1
        return True

    for i in range(start_y, start_y + length_arr):
        for j in range(start_x, start_x + length_arr):
            if point != arr[i][j]:
                return False
    if point == 1:
        blue += 1
    else:
        white += 1
    return True


def func(arr, start_x, start_y, length_arr):
    if check(arr, start_x, start_y, length_arr):
        return
    else:
        len_arr = length_arr//2
        func(arr, start_x, start_y, len_arr)
        func(arr, start_x, start_y+len_arr, len_arr)
        func(arr, start_x+len_arr, start_y,len_arr)
        func(arr, start_x+len_arr, start_y+len_arr,len_arr)
        

input = sys.stdin.readline
n = int(input())
arr = []
blue = 0
white = 0
for i in range(n):
    arr.append(list(map(int,input().split())))
func(arr,0,0,n)
print(white)
print(blue)