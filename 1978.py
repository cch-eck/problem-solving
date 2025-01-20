# 에라토스테네스의 체
import math

def prime(num: int):
    if num<=1: 
        return False
    for m in range(2, int(math.sqrt(num))+1):
        if num % m == 0:
            return False
    return True

num_inputs = int(input())
nums = list(map(int, input().split()))
prime_count = sum(1 for n in nums if prime(n))
print(prime_count)