import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    k = int(sys.stdin.readline())
    li.append(k)
li.sort()
print(round(sum(li)/n))
print(li[n//2])
counter = Counter(li)
max_frequency = max(counter.values())
max_key = [(key ,value) for key,value in counter.items() if value == max_frequency]
if len(max_key) >= 2:
    max_key.sort(key = lambda x : x[0])
    print(max_key[1][0])
else:
    print(max_key[0][0])
print(max(li) - min(li))