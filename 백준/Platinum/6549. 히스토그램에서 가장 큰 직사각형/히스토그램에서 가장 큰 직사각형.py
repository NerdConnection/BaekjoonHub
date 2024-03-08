import sys
input = sys.stdin.readline
while True:
    n,*temp = list(map(int, input().split()))
    if  n == 0:
        break
    else:
        histogram = [0] + temp + [0]
        checked = [0]
        area = 0

        for i in range(1,n+2):
            while checked and histogram[checked[-1]] > histogram[i]:
                current = checked.pop()
                area = max(area, (i-(checked[-1]+1))*histogram[current])
            checked.append(i) 
        print(area) 