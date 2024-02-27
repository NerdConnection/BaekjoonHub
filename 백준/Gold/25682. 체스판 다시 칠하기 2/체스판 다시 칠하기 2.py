import sys

n,m,k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

sum_b = [[0]*(m+1) for _ in range(n+1)]
sum_w = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if (i+j)%2 == 0:
            if arr[i][j] == 'B':
                sum_b[i+1][j+1] = 1 + sum_b[i][j+1] + sum_b[i+1][j] - sum_b[i][j]
                sum_w[i+1][j+1] = sum_w[i][j+1] + sum_w[i+1][j] - sum_w[i][j]
            else:
                sum_b[i+1][j+1] = sum_b[i][j+1] + sum_b[i+1][j] - sum_b[i][j]
                sum_w[i+1][j+1] = 1 + sum_w[i][j+1] + sum_w[i+1][j] - sum_w[i][j]
        else:
            if arr[i][j] == 'B':
                sum_b[i+1][j+1] = sum_b[i][j+1] + sum_b[i+1][j] - sum_b[i][j]
                sum_w[i+1][j+1] = 1 + sum_w[i][j+1] + sum_w[i+1][j] - sum_w[i][j]
            else:
                sum_b[i+1][j+1] = 1 + sum_b[i][j+1] + sum_b[i+1][j] - sum_b[i][j]
                sum_w[i+1][j+1] = sum_w[i][j+1] + sum_w[i+1][j] - sum_w[i][j]

res = float('inf')
for i in range(k,n+1):
    for j in range(k,m+1):
        s_i = i - k + 1
        s_j = j - k + 1
        tmp = min(sum_b[i][j] - sum_b[i][s_j-1] - sum_b[s_i-1][j] + sum_b[s_i-1][s_j-1],sum_w[i][j] - sum_w[i][s_j-1] - sum_w[s_i-1][j] + sum_w[s_i-1][s_j-1])

        if tmp < res:
            res = tmp
print(res)