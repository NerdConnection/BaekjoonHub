import sys 

def merge_sort(arr,p,r , x,k):
    if p < r:
        q = (p+r)//2
        merge_sort(arr,p,q,x,k)
        merge_sort(arr,q+1,r,x,k)
        merge(arr,p,q,r,x,k)


def merge(arr,p,q,r,x,k):
    i = p
    j= q+1
    t = 0
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            t+=1
            i+=1
        else:
            tmp[t] = arr[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = arr[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = arr[j]
        t += 1
        j += 1

    for y in range(len(tmp)):
        arr[p + y] = tmp[y]
        x[0] += 1
        if x[0] == k:
            x.append(tmp[y])


n, k = map(int, (sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
x = [0]
merge_sort(arr,0,len(arr)-1,x,k)
if k <= x[0]:
    print(x[1])
else:
    print(-1)