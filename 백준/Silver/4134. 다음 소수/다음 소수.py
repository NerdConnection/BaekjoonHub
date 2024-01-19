import math

def is_prime(number):
    sqrt_number = int(math.sqrt(number))
    for i in range(2,sqrt_number+1):
        if number%i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    number = int(input())
    if number < 2:
        print(2)
        continue
    while is_prime(number) == False:
        number += 1
    print(number)