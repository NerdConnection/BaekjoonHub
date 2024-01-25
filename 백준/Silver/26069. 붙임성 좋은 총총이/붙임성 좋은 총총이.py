import sys

n = int(sys.stdin.readline())
flag = 0
li = set()
li2 = {"ChongChong"}
for _ in range(n):
    a,b = sys.stdin.readline().rstrip().rsplit()
    
    li.add(a)
    li.add(b)
    if li & li2:
        li2.add(a)
        li2.add(b)
    li.clear()
print(len(li2))