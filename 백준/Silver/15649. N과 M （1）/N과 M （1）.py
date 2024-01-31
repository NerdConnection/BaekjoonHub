import sys

def func(m, num_list,arr,visited):

    if m == 0:
        for a in arr:
            print(a, end = " ")
        print()
    else:
        for x in num_list:
            if x not in visited:
                arr.append(x)
                visited.append(x)
                func(m-1,num_list,arr,visited)
                arr.pop()
                visited.pop()

n,m = map(int, sys.stdin.readline().split())
num_list = list(range(1,n+1))
arr = []
visited = []
func(m,num_list,arr,visited)
