import sys

n = int(sys.stdin.readline())
arr = []
dp = [0]*n
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
elif n == 3:
    print(max(arr[1]+arr[2] , arr[0]+arr[2], arr[0]+arr[1]))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1]+arr[2], dp[1])
    for i in range(3,n):
        dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3],dp[i-1])
    print(dp[n-1])

