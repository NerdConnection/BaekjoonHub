import sys
s = list(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline())
arr = [[0]*26 for _ in range(len(s))]

arr[0][ord(s[0])-97] =1
for i in range(1,len(s)):
    arr[i][ord(s[i])-97] = 1
    for j in range(26):
        arr[i][j] += arr[i-1][j]

for _ in range(q):
    a,l,r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    if l > 0:
        res = arr[r][ord(a)-97] - arr[l-1][ord(a)-97] 
    else:
        res = arr[r][ord(a)-97]
    print(res)