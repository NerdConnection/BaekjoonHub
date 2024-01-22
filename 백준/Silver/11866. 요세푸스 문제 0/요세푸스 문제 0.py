n,k = map(int,(input().split()))
li = list(range(1,n+1))
sol = []
idx = 0

while li:
    idx += k-1
    if idx >= len(li):
        idx %= len(li)
    sol.append(str(li.pop(idx)))

print("<", ", ".join(sol), ">", sep="")