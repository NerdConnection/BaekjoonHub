import sys


def func(start):
    if len(arr) == m:
        print(*arr)
        return
    
    else:
        for i in range(start,n+1):
            if i not in arr:
                arr.append(i)
                func(i)
                arr.pop()

arr = []    
n,m = map(int, sys.stdin.readline().split())
func(1)
