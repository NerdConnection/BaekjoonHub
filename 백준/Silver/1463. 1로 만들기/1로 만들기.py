import sys

n = int(sys.stdin.readline())
dp = [0,0,1,1] + [0 for _ in range(n-3)]

for i in range(4,n+1):
    if i%2==0 and i%3==0:
        dp[i] = min(dp[i-1]+1 , dp[i//2]+1, dp[i//3]+1)
    elif i%2 == 0:
        dp[i] = min(dp[i-1]+1 , dp[i//2]+1)
    elif i%3 == 0:
        dp[i] = min(dp[i-1]+1 , dp[i//3]+1)
    else:
        dp[i] = dp[i-1]+1

print(dp[n])