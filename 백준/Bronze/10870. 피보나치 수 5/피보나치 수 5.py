import sys

def pibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pibonachi(n-2) + pibonachi(n-1)
n = int(sys.stdin.readline())
print(pibonachi(n))