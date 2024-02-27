import sys
input = sys.stdin.readline

n,k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

res = 0
for _ in range(n):
    value = arr.pop()
    if value > k:
        continue
    else:
        d = k//value
        res += d
        remain = k%value
        k = remain
print(res)