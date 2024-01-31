import sys

def func(m, num_list,arr,visited):

    if m == 0:
        arr_set = set(arr)
        if arr_set not in arr_set_list:
            arr_set_list.append(arr_set)
            print(*arr)
        return
        
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
arr_set_list = []
func(m,num_list,arr,visited)
