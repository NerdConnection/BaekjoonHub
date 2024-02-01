import sys


def func(arr):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1,n+1):
        if len(arr) != 0 and i < arr[-1]:
            pass
        else:
            arr.append(i)     
            func(arr)
            arr.pop()
            
arr = []    
n,m = map(int, sys.stdin.readline().split())
func(arr)
