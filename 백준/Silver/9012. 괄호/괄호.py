import sys
n = int(input())
for _ in range(n):
    li = list(sys.stdin.readline().strip())
    stack = []
    for word in li:
        if word == '(':
            stack.append('(')
        else :
            if not stack:
                print("NO")
                break
            stack.pop()
    else:
        if len(stack) == 0:
            print("YES")
        else :
            print("NO")


