import sys
from collections import Counter

# 풀이 1
input = sys.stdin.readline
n,m = map(int,(input().split()))
tree_list = Counter(map(int,input().split()))
max_h = max(tree_list)
min_h = 1

while min_h <= max_h:
    mid = (min_h+max_h)//2
    tree = sum((h - mid)*i for h, i in tree_list.items() if h >mid)
    if tree < m:
        max_h = mid -1
    else:
        min_h = mid + 1

print(max_h)