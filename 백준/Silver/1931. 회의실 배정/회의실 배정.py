import sys
input = sys.stdin.readline
n = int(input())
arr = []
max_end = float('-inf')

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
arr.sort(key = lambda x : x[1])
end = -1
res = 0

for i in arr:
    s = i[0]
    e = i[1]
    if s >= end and e >= end:
        res += 1
        end = e

print(res)