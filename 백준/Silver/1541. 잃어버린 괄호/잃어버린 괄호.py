import sys
input = sys.stdin.readline
exp = input().rstrip().split('-')

for i in range(len(exp)):
    if '+' in exp[i]:
        li = exp[i].split('+')
        exp[i] = sum(list(map(int,li)))
res = int(exp[0])
for i in range(1,len(exp)):
    res -= int(exp[i])
print(res)