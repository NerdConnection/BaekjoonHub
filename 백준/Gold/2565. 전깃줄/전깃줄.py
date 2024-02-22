import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr.sort()
dp = [1]*n
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(len(dp) - max(dp))