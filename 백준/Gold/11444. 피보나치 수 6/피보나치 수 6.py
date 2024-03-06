import sys
# https://jja08111.github.io/algorithm/baekjoon-2749-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-3/
# 피보나치 수열 => 행렬의 거듭제곱 이용
# 피보나치 수열을 행렬로 나타내면
# =>
# [fn,    =  [[1,1] [fn-1
#  fn-1,]      [1,0]]  fn-2]

 # Xn          A     Xn-1
# [fn,    =  [[1,1] [fn-1
#  fn-1,]      [1,0]]  fn-2]

 # Xn          A^n-1   X1
# [fn,    =   [[1,1]   [[1]
#  fn-1,]      [1,0]]  [0]]


# x3          x2

# f3          f2
# f2   A      f1


# x3          x1

# f3          f1
# f2   A^2    f0

def mul(a,b):
    row = len(a)
    col = len(b[0])
    x = [[0]*(col) for _ in range(row)]
    for i in range(row):
        for j in range(col):
            sum = 0
            for k in range(len(b)):
                sum += a[i][k] * b[k][j]
            x[i][j] = sum%1000000007
    return x

def power(arr,n):
    if n == 1:
        return arr

    tmp = power(arr, n//2)
    if n % 2 == 0:
        return mul(tmp,tmp)
    else:
        return mul(mul(tmp,tmp), arr)

n = int(sys.stdin.readline())
if n < 3:
    print(1)
else:
    mat = [[1,1],[1,0]]
    res = mul(power(mat,n-1), [[1],[0]])
    print(res[0][0])
