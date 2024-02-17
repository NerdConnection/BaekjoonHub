import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp_arr = [0]*n
dp_arr[0] = arr[0]

def dp(n):
    for i in range(1,n):
        dp_arr[i] = max(dp_arr[i-1] + arr[i], arr[i])
    return max(dp_arr)

print(dp(n))
