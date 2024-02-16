import sys
n = int(sys.stdin.readline())
arr = [5,8]
if n == 5:
    print(5,3)
elif n == 6:
    print(8,4)
else:
    for i in range(2,n-4):
        arr.append(arr[i-1] + arr[i-2])
    print(arr[n-5],n-2)