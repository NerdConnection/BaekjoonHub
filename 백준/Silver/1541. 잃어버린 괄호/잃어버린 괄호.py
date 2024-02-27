import sys
input = sys.stdin.readline
arr = input().rstrip()
arr2 = []
current=''
for char in arr:
    if char.isdigit():
        current += char
    else:
        arr2.append(int(current))
        current = ''
        arr2.append(char)
arr2.append(int(current))
arr3 = []
for i in range(len(arr2)):
    if arr2[i] == '+':
        arr2[i+1] = (arr2[i-1] + arr2[i+1])
        arr2[i-1] = 0

for i in range(len(arr2)):
    if arr2[i] != 0 and arr2[i] != '+':
        arr3.append(arr2[i])

if len(arr3) == 1:
    print(arr3[0])
else:
    res = ''
    for i in range(len(arr3)):
        res += str(arr3[i])
    print(eval(res))
