import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = [arr[0]]+[0]*(n-1)
for i in range(1,n):
    arr2[i] = arr2[i-1] + arr[i]
for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    if i == 1:
        sum = arr2[j-1]
        print(sum)
    else:
        sum = arr2[j-1] - arr2[i-2]
        print(sum)