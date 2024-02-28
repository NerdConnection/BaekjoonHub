import sys
input = sys.stdin.readline
n = int(input())
distance = list(map(int, input().split()))
gas_value = list(map(int, input().split()))
min_gas_value = gas_value[0]
res = 0

for i in range(n-1):
    if gas_value[i] < min_gas_value:
        min_gas_value = gas_value[i]
    res += min_gas_value * distance[i]
print(res)