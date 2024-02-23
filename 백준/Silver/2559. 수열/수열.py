import sys

n,k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
idx_arr = [0]*(n-k+1)

for i in range(k):
    idx_arr[0] += arr[i]

for i in range(1,len(idx_arr)):
    idx_arr[i] = idx_arr[i-1] - arr[i-1] + arr[k+i-1]

print(max(idx_arr))