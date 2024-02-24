import sys

s = list(sys.stdin.readline().rstrip())
q = int(sys.stdin.readline())
dic = {}
for i,char in enumerate(s):
    if char in dic.keys():
        dic[char].append(i)
    else:
        dic[char] = [i]

for _ in range(q):
    a,l,r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    res = 0
    if a in dic.keys():
        li = dic[a]
        for idx in li:
            if l<= idx and idx<=r:
                res += 1
        print(res) 
    else:
        print(res)