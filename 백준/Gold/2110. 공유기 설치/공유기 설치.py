import sys
# 정답 풀이
input = sys.stdin.readline
n,c = map(int,(input().split()))
house_loc =[]
for _ in range(n):
    house_loc.append(int(input()))
house_loc.sort()

start = 1
end = house_loc[-1] - house_loc[0]
res = 0
if c == 2:
    print(end)
else:
    while start <= end:
        mid = (start + end) // 2
        current = house_loc[0]
        temp = 1
        for i in range(1,len(house_loc)):
            if house_loc[i] >= mid + current:
                temp += 1
                current = house_loc[i]
        
        if temp < c:
            end = mid - 1 
        else:
            start = mid + 1
            res = mid
    print(res)