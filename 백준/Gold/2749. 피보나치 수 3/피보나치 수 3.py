import sys
n = int(sys.stdin.readline())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    m = 1000000
    p = 15*(m//10)
    remain = n%p
    arr = [0,1]+[0]*(remain-1)
    
    for i in range(2,remain+1):
        arr[i] = ((arr[i-2]%m) + (arr[i-1]%m))%m
    print(arr[remain])