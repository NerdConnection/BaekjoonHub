import sys
n = int(input())
for _ in range(n):
    li = list(sys.stdin.readline().strip())
    check = 0
    flag = 0
    for word in li:
        if word == '(':
            check += 1
        else :
            check -= 1
            if check < 0:
                print("NO")
                flag = 1
                break
    
    if flag == 1:
        pass
    
    else:                        
        if check == 0:
            print("YES")
        else:
            print("NO")


