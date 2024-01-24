import sys
n = sys.stdin.readline()
li = list(map(int,sys.stdin.readline().split()))
print(max(li) * min(li))