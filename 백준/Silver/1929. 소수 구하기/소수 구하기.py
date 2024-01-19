import math

def is_prime(number):
    sqrt_number = int(math.sqrt(number))
    for i in range(2,sqrt_number+1):
        if number%i == 0:
            return False
    return True


m,n = map(int, input().split())

for number in range(m,n+1):
    if number < 2:
        continue
    if is_prime(number) is True:
        print(number)
