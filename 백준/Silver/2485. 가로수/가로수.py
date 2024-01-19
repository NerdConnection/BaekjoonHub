def GCD(a,b):
    max_num = max(a,b)
    min_num = min(a,b)

    if max_num%min_num == 0:
        return min_num
    else:
        return GCD(min_num,max_num%min_num)
    
n = int(input())
pos = [int(input()) for _ in range(n)]
pos_diff = [ (pos[i+1] - pos[i]) for i in range(len(pos)-1)]

gcd = pos_diff[0]
for diff in pos_diff[1:]:
    gcd = GCD(gcd, diff)

res = sum((pos[i + 1] - pos[i]) // gcd - 1 for i in range(len(pos) - 1))
print(res)