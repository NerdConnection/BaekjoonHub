import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

arr.reverse()
dp2 = [0]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[j] + 1, dp2[i])
dp2.reverse()
for i in range(n):
    dp[i] += dp2[i]
print(max(dp))