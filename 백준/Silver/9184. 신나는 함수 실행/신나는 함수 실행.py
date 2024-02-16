import sys


def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    else:
        for x in range(1,a+1):
            for y in range(1,b+1):
                for z in range(1,c+1):  
                    if x< y and y < z:
                        dp[z][x][y] = dp[z-1][x][y] + dp[z-1][x][y-1] - dp[z][x][y-1]
                    else:
                        dp[z][x][y] = dp[z][x-1][y] + dp[z][x-1][y-1] + dp[z-1][x-1][y] - dp[z-1][x-1][y-1]

        return dp[c][a][b]

while True:
    a,b,c = map(int,(sys.stdin.readline().split()))
    dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
    
    if a == -1 and b == -1 and c == -1:
        break 
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
