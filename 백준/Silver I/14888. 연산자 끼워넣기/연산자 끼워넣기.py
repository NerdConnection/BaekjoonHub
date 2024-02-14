import sys


def bt(i, res):
    global add,sub,mul,div,max_num,min_num
    if i == n:
        max_num = max(res,max_num)
        min_num = min(res,min_num)
    else:
        if add > 0:
            add-=1
            bt(i+1, res + num_list[i])
            add+=1
        if sub > 0:
            sub -=1
            bt(i+1, res - num_list[i])
            sub += 1
        if mul > 0:
            mul -= 1
            bt(i+1, res * num_list[i])
            mul += 1
        if div > 0:
            div -= 1
            bt(i+1, int(res / num_list[i]))
            div += 1



n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
add,sub,mul,div = map(int, sys.stdin.readline().split())
max_num = -1e9
min_num = 1e9
bt(1,num_list[0])

print(max_num)
print(min_num)