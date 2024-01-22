from collections import deque

n = int(input())
li = deque(list(range(1,n+1)))

while len(li) != 1:
    li.popleft()
    li.append(li.popleft())

print(li[0])