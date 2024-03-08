import sys

input = sys.stdin.readline
n = int(input())
arr = list(input().split())
m = int(input())
arr2 = list(input().split())
dic = {}
for num in arr:
    if num in dic.keys():
        dic[num] += 1
    else:
        dic[num] = 1

for num in arr2:
    if num in dic.keys():
        print(dic[num],end=' ')
    else:
        print(0,end = ' ')