import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,n):
    for k in range(len(arr[i])):
        if k == 0:
            arr[i][k] += arr[i-1][k]
        
        elif k == len(arr[i]) - 1:
            arr[i][k] += arr[i-1][k-1]
        
        else:
            arr[i][k] += max(arr[i-1][k-1], arr[i-1][k])

print(max(arr[n-1]))