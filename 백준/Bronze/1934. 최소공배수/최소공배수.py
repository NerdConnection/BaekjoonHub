def GCD(a,b):
    if a%b == 0:
        return b
    else:
        return GCD(b,a%b)

n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    gcd = GCD(b,a)
    lcm = a*b//gcd
    print(lcm)