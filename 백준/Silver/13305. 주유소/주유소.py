import sys
input = sys.stdin.readline
n = int(input())
distance = list(map(int, input().split()))
gas_value = list(map(int, input().split()))
result = 0
gas_value.pop() # 마지막 도시 gas value 삭제

while distance:
    x = gas_value.index(min(gas_value))
    dis = 0
    for i in range(x,len(distance)):
        dis += distance[i]
    result += min(gas_value) * dis
    distance = distance[:x]
    gas_value = gas_value[:x]
print(result)