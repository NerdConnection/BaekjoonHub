import sys
input = sys.stdin.readline
n,k = map(int,(input().split()))
p = 1000000007


def factorial(n):
    res = 1
    for i in range(2,n+1):
        res = res * i % p
    return res

def power(n,k):
    if k == 1:
        return n%p
    if k%2 == 0:
        return power(n,k//2) ** 2 % p
    else:
        return power(n,k//2) ** 2 *n %p
    

top = factorial(n)
bottom = factorial(n-k)%p * factorial(k) %p
print(top * power(bottom,p-2) % p)