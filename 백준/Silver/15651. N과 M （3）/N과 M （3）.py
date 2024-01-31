import sys

def print_permutations(n, m):
    if m == 1:
        for i in range(1, n + 1):
            print(i)
    elif m == 2:
        for i in range(1, n + 1):
            for h in range(1, n + 1):
                print(i, h)
    elif m == 3:
        for i in range(1, n + 1):
            for h in range(1, n + 1):
                for k in range(1, n + 1):
                    print(i, h, k)
    elif m == 4:
        for i in range(1, n + 1):
            for h in range(1, n + 1):
                for k in range(1, n + 1):
                    for l in range(1, n + 1):
                        print(i, h, k, l)
    elif m == 5:
        for i in range(1, n + 1):
            for h in range(1, n + 1):
                for k in range(1, n + 1):
                    for l in range(1, n + 1):
                        for p in range(1, n + 1):
                            print(i, h, k, l, p)
    elif m == 6:
        for i in range(1, n + 1):
            for h in range(1, n + 1):
                for k in range(1, n + 1):
                    for l in range(1, n + 1):
                        for p in range(1, n + 1):
                            for q in range(1, n + 1):
                                print(i, h, k, l, p, q)
    elif m == 7:
        for i in range(1, n + 1):
            for h in range(1, n + 1):
                for k in range(1, n + 1):
                    for l in range(1, n + 1):
                        for p in range(1, n + 1):
                            for q in range(1, n + 1):
                                for r in range(1, n + 1):
                                    print(i, h, k, l, p, q, r)

n, m = map(int, sys.stdin.readline().split())
print_permutations(n, m)
