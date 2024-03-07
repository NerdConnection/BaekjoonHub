import sys

def binary_search(arr,left ,right ,value):
    if left <= right:
        mid = (left + right) //2
        if arr[mid] == value:
            return 1
        elif arr[mid] < value:
            return binary_search(arr,mid+1,right,value)
        else:
            return binary_search(arr,left,mid-1,value)
    return 0

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for value in arr2:
    print(binary_search(arr,0 ,len(arr) - 1, value))