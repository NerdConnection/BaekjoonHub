import sys

def mul(arr,arr2):
    x = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                x[i][j] += arr[i][p] * arr2[p][j] % 1000
    return x

def power(arr,k):
    if k == 1:
        return arr
    
    temp = power(arr, k//2)
    if k % 2 == 0:
        return mul(temp,temp)
    else:
        return mul(mul(temp,temp),arr)
    
input = sys.stdin.readline
n,b = map(int,(input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
res = power(arr,b)
for i in range(n):
    for j in range(n):
        res[i][j] = res[i][j] %1000
for a in res:
    print(*a)