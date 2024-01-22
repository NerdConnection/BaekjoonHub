import sys

input = sys.stdin.readline
n = int(input().rstrip())
queue = [0]*2000001
head = tail = 0

for _ in range(n):
    commend = input().rstrip().split()

    if commend[0] == 'push':
        tail += 1
        queue[tail] = int(commend[1])
        

    elif commend[0] == 'pop':
        if tail - head > 0 :
            print(queue[head+1])
            head += 1
        else:
            print(-1)

    elif commend[0] == 'size':
        print(tail - head)
    
    elif commend[0] == 'empty':
        if tail - head > 0 :
            print(0)
        else:
            print(1)

    elif commend[0] == 'front':
        if tail - head > 0:
            print(queue[head+1])
        else:
            print(-1)
    elif commend[0] == 'back':
        if tail - head > 0:
            print(queue[tail])
        else:
            print(-1)