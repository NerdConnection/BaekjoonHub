import sys

n = int(sys.stdin.readline())
arr = [0] * 1000001
arr[1] = 1
arr[2] = 2

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3,n+1):
            arr[i] = (arr[i-2] + arr[i-1])  % 15746
        return arr[n]

print(dp(n))



