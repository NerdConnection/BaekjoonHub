import sys

input = sys.stdin.readline
n,m = map(int,(input()).split())
arr = []
arr2 = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
m,k = map(int,(input()).split())
for _ in range(m):
    arr2.append(list(map(int,input().split())))

arr3 = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for p in range(m):
            arr3[i][j] += arr[i][p] * arr2[p][j]

for i in range(n):
    for j in range(k):
        print(arr3[i][j], end = ' ')
    print()
