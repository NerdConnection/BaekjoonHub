from collections import deque
import sys
n = int(sys.stdin.readline())
arr1 = sys.stdin.readline().split()
arr2 = sys.stdin.readline().split()
arr3 =deque()
for i in range(n):
    if arr1[i] == '0':
        arr3.append(arr2[i])

m = int(sys.stdin.readline())
for value in sys.stdin.readline().split():
    arr3.appendleft(value)
    print(arr3.pop(), end = " ")