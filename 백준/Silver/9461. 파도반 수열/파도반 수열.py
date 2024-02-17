import sys

def dp(n):
    if arr[n]:
        return arr[n]
    else:
        arr[n] = dp(n-5) + dp(n-1)
        return arr[n]
T = int(sys.stdin.readline())
arr = [0] *101
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

arr[6] = 3
arr[7] = 4
arr[8] = 5
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp(n))