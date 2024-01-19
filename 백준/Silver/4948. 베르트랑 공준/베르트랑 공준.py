import math

def is_prime(number):
    if number < 2:
        return False
    sqrt_number = int(math.sqrt(number))
    for i in range(2,sqrt_number+1):
        if number%i == 0:
            return False
    return True



prime_list = [False]
for i in range(1,246913):
    if is_prime(i) == True:
        prime_list.append(True)
    else :
        prime_list.append(False)

while True:
    n = int(input())
    if n == 0:
        break
    res = 0
    for i in range(n+1, 2*n+1):
        if prime_list[i] == True:
            res +=1
    print(res)
