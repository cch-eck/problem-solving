# import random
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
A = [num % 2 for num in A]

print(A)
answer = N
i, j = 0,0

# 홀짝성이 같은 구간에서는 수를 하나만 뽑는다.
while i < N-1:
    print(i,j)
    while (i+j+1 < N and A[i] == A[i+j+1] ):
        print(f'A[{i}] = A[{i+j}] = {A[i]}')
        j += 1
    answer = answer -j
    i = i + j + 1
    j = 0
print(answer)

#[1 0 1 0 1 0]