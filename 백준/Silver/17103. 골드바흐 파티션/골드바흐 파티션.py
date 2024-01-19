# 에라토스테네스의 체 활용
prime_num_list = [False,False]+[True]*999999
for i in range(2,1000001):
    if prime_num_list[i]:
        for j in range(i*2,1000001,i):
            prime_num_list[j] = False

test_case_num = int(input())
for _ in range(test_case_num) :
    num = int(input())
    if num < 4:
        print(0)
        continue
    else:
        res = 0 
        for i in range(2,num//2+1):
            if  prime_num_list[i] and prime_num_list[num-i]:
                res += 1
    print(res)
