n = int(input())
queue = list(map(int, input().split()))
stack = []
take_snake_line = []
sequence = 1
for k in queue:
    if k == sequence:
        take_snake_line.append(k)
        sequence += 1
    else:
        stack.append(k)

    if stack:
        while stack[-1] == sequence :
            take_snake_line.append(stack.pop())
            sequence += 1
            if len(stack) == 0:
                break

for i in range(len(stack)):
    take_snake_line.append(stack.pop())

flag = 0
for i in range(1,n+1):
    if take_snake_line[i-1] != i:
        flag = 1
        break

if flag == 0:
    print("Nice")
else :
    print("Sad")
