import sys
input = sys.stdin.readline
a,b,c = map(int,(input().split()))

def mul(a,n):
    if n == 1:
        return a%c
    if n % 2 == 0:
        return (mul(a,n//2) **2 % c)
    else:        
        return ((mul(a,n//2) **2 *a )% c)

print(mul(a,b))