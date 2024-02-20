import sys
def rec(n):
    if n in dp:
        return dp[n]
    res = 1+ min(rec(n//3) + n%3 , rec(n//2) + n%2)
    dp[n] = res
    return res
dp = {1:0, 2:1}
n = int(sys.stdin.readline())
print(rec(n))