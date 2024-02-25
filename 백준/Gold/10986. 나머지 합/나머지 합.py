import sys
import math
n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# idx => 나머지 값을 의미하는 배열 생성
remainder_arr = [0]*m 
remainder_arr[arr[0]%m] += 1

# 누적합을 나머지에 따라 배열에 저장
for i in range(1,n):
    arr[i] = (arr[i-1] + arr[i]) % m
    remainder_arr[arr[i]] += 1

# 조합으로 경우의 수 생성 , 나머지가 0인경우가 디폴트
res = remainder_arr[0]
for i in range(m):
    if remainder_arr[i] >= 2:
        res += math.comb(remainder_arr[i],2)
print(res)
