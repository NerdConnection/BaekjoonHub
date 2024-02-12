import sys

def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x]-rows[i]) == abs(x-i):
            return False
    return True

def chess(x):
    global res

    
    if x == n:
        res += 1
        return
    else:
        for i in range(n):
            rows[x] = i
            if check(x):
                chess(x+1)


n = int(input())
rows = [0] * n
res = 0
chess(0)
print(res)