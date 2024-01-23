from collections import deque
import sys

n = int(input())
dequeue = deque()
for _ in range(n):
    command = list(map(int,(sys.stdin.readline().split())))
    if command[0] == 1:
        dequeue.appendleft(command[1])
    elif command[0] == 2:
        dequeue.append(command[1])
    elif command[0] == 3:
        if dequeue:
            print(dequeue.popleft())
        else:
            print(-1)
    elif command[0] == 4:
        if dequeue:
            print(dequeue.pop())
        else:
            print(-1)
    elif command[0] == 5:
        print(len(dequeue))
    elif command[0] == 6:
        if not dequeue:
            print(1)
        else:
            print(0)
    elif command[0] == 7:
        if dequeue:
            print((dequeue[0]))
        else:
            print(-1)
    elif command[0] == 8:
        if dequeue:
            print(dequeue[-1])
        else:
            print(-1)