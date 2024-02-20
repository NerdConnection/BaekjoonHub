import sys

n = int(sys.stdin.readline())
arr = [[1]*10]+[[0]*10 for x in range(n-1)]
arr[0][0] = 0
for k in range(1,n):
    for i in range(10):
        if i == 0:
            arr[k][i+1] += arr[k-1][i]
            arr[k][i+1]%=1000000000
        elif i == 9:
            arr[k][i-1] += arr[k-1][i]
            arr[k][i-1]%=1000000000
        else:
            arr[k][i-1] += arr[k-1][i]
            arr[k][i+1] += arr[k-1][i]
            arr[k][i+1]%=1000000000
            arr[k][i-1]%=1000000000

print(sum(arr[n-1])%1000000000)