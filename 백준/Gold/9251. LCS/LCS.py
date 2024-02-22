import sys
arr1 =[0]+list(sys.stdin.readline().rstrip())
arr2 =[0]+list(sys.stdin.readline().rstrip())

dp = [[0]*len(arr1) for _ in range(len(arr2))]

for i in range(1,(len(arr2))):
    for j in range(1,(len(arr1))):
        if arr2[i] == arr1[j]:
            a = 1
        else:
            a = 0
        dp[i][j] = max(dp[i-1][j-1]+a, dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
