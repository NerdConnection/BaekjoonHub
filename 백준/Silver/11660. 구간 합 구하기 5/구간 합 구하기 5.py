import sys
# 2차원 배열에 문제에 맞게 누적합을 저장하고
#  res = sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + arr[x1-1][y1-1]



n,m = map(int, sys.stdin.readline().split())
arr = []
sum_arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    arr.append(li)

for i in range(1,n+1):
    for j in range(1,n+1):
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    res = sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1]
    print(res)