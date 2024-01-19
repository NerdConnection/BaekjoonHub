n = int(input())
li =list(map(int , input().split()))
li_sorted = sorted(set(li))

li_map = {}
for i in range(len(li_sorted)):
    li_map[li_sorted[i]] = i

for value in li:
    print(li_map[value],end=' ')