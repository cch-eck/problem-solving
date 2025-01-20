def ceil(n: float) -> int:
    if n == n//1:
        return int(n)
    else:
        return int(n+1)

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for i in range(N):
    left = A[i]-B
    answer += 1
    if left>0:
        answer += (left + C - 1) // C
print(answer)