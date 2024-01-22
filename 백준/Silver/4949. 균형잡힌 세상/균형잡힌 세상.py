import sys

while(True):
    stack = []
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    s = list(s)
    flag = 0

    for word in s:
        if word == ')':
            if len(stack) == 0 or stack.pop() != '(':
                flag = 1
                break
        if word == ']':
            if len(stack) == 0 or stack.pop() != '[':
                flag = 1
                break
        
        if word == '(':
            stack.append(word)
        
        if word == '[':
            stack.append(word)
    

    if flag == 0 and len(stack) == 0:
        print("yes")
    else :
        print("no")
