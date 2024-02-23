import sys

n,k = map(int, sys.stdin.readline().split())
arr = [[0,0]]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
bag = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w = arr[i][0]
    v = arr[i][1]
    for j in range(1,k+1):
        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j-w]+v, bag[i-1][j])
print(bag[-1][-1])