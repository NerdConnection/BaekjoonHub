import sys

input = sys.stdin.readline
k,n = map(int,(input().split()))
wire_list = []
for _ in range(k):
    wire_list.append(int(input()))

max_len = max(wire_list)
min_len = 1
while min_len <= max_len:
    mid = (max_len+min_len)//2
    res = 0
    for i in wire_list:
        res += i//mid

    if res >= n:
        min_len = mid + 1 
    else:
        max_len = mid - 1
print(max_len)