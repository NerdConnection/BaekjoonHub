from collections import deque
import sys

n = int(input())
li = list(map(int,sys.stdin.readline().split()))
li_with_idx = [(value, idx)for idx,value in enumerate(li)]
dequeue = deque(li_with_idx)
sequence_list = []

while dequeue:
    idx_add ,idx=dequeue.popleft()
    sequence_list.append(idx+1)
    if idx_add > 0:
        dequeue.rotate(-(idx_add-1))
    else:
        dequeue.rotate(-(idx_add))
for i in sequence_list:
    print(i,end=" ")

